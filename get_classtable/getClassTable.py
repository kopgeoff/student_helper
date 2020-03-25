import requests
import re
import sys


class CustomerError(Exception):
    def __init__(self, error_info):
        super().__init__(self)
        self.errorInfo = error_info

    def __str__(self):
        return self.errorInfo


class GetClassTable:
    # param in requests
    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
        self.cookies = None
        self.session = None
        self.login_param = {}
        self.class_param = {}
        self.text = ""
        self.class_plan = []

    # create a session
    def start_session(self):
        self.session = requests.session()

    # get random param and save information of login
    def login(self, uid, password):
        try:
            html_login = self.session.get(
                "https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fportal.neu.edu.cn%2Ftp_up%2F",
                headers=self.header)
            # get hidden param
            data = re.findall('<input type="hidden"(.*?)/>', html_login.text, re.DOTALL)
            # get param with value
            for key in data:
                temp = re.findall('value="(.*?)"', key, re.DOTALL)
                if len(temp) == 1:
                    te = re.findall('name="(.*?)"', key, re.DOTALL)
                    if len(te) == 1:
                        self.login_param[te[0]] = temp[0]
                    else:
                        # please connect it to feedback
                        raise CustomerError("LoadError:Structure of html has been changed.")
                else:
                    continue
            # rsa = uid + password + lt(which is in hidden)
            self.login_param["rsa"] = str(uid) + str(password) + self.login_param["lt"]
            self.login_param["ul"] = str(len(str(uid)))
            self.login_param["pl"] = str(len(str(password)))
            # login in
            htm = self.session.post(
                "https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fportal.neu.edu.cn%2Ftp_up%2F",
                data=self.login_param, headers=self.header)
            self.cookies = htm.cookies
            if "我的首页" not in htm.text:
                raise CustomerError("Exist error in id or password。")
            # return "Vpn login is successful."
            return True
        except requests.exceptions.ConnectionError:
            # return "Please check your network connection."
            return False
        except CustomerError:
            # set kinds of errors and return different string
            # return str(e)
            return False
        except:
            return False

    def get_class(self, cid):
        try:
            # enter the teaching system
            home_page = self.session.get(
                "http://219.216.96.4/eams/homeExt.action", cookies=self.cookies, headers=self.header)
            self.cookies = home_page.cookies
            # get student id in database
            class_table = self.session.get(
                "http://219.216.96.4/eams/courseTableForStd.action", cookies=self.cookies, headers=self.header)
            sid = re.findall('"ids","(.*?)"', class_table.text, re.DOTALL)
            # remove another id specially
            for i in sid:
                if i == "3075":
                    sid.remove(i)
                else:
                    continue
            # except system update
            if len(sid) == 1:
                self.class_param["ids"] = sid[0]
            # add post param
            self.class_param["ignoreHead"] = "1"
            self.class_param["showPrintAndExport"] = "1"
            self.class_param["setting.kind"] = "std"
            self.class_param["startWeek"] = ""
            self.class_param["semester.id"] = str(cid)
            self.class_param["project.id"] = "1"
            # update cookies
            self.header["Referer"] = "http://219.216.96.4/eams/courseTableForStd!courseTable.action"
            new_table = self.session.post(
                "http://219.216.96.4/eams/courseTableForStd!courseTable.action",
                data=self.class_param, cookies=self.cookies, headers=self.header)
            self.cookies = new_table.cookies
            # last page value is "js", so use "print" to get information of class
            table = "http://219.216.96.4/eams/courseTableForStd!courseTable.action?setting.kind=std&ids=" +\
                    self.class_param["ids"]
            hh_hh = self.session.get(table, cookies=self.cookies, headers=self.header)
            # to do text split to get position of class in a week
            self.text = hh_hh.text
            return True
        except requests.exceptions.ConnectionError:
            # return "Please check your network connection."
            return False
        except CustomerError:
            # set kinds of errors and return different string
            # return str(e)
            return False
        except:
            return False

    def stop_session(self):
        self.session.close()

    def parse_class(self):
        try:
            content = self.text.split("var unitCount")[1].split("</script>")[0]
            unit_class = content.split("var teachers")
            if len(unit_class) == 1:
                pass
            else:
                unit_class = unit_class[1:]
                total = []
                for i in range(len(unit_class)):
                    unit_class[i] = "var teachers" + unit_class[i]
                    unit_class[i] = unit_class[i].replace("\r", "").replace("\t", "").replace("\n", "").replace("}", "")
                    temp = unit_class[i].split(";")
                    total.append(temp)
                for j in range(len(total)):
                    for k in range(len(total[j])-1, -1, -1):
                        if len(total[j][k]) >= 8 and total[j][k][:8] == "activity":
                            total[j][k] = "@#@".join(re.findall('"(.*?)"', total[j][k], re.DOTALL)[:5])
                            continue
                        elif len(total[j][k]) >= 5 and total[j][k][:5] == "index":
                            total[j][k] = str(eval(total[j][k].split("=")[-1].replace("unitCount", "12")))
                            continue
                        else:
                            total[j].remove(total[j][k])
                    te = dict()
                    te['cid'], te['cname'], te['pid'], te['pname'], te['week'] = total[j][0].split("@#@")
                    te1 = []
                    for t in range(1, len(total[j])):
                        te1.append(total[j][t])
                    te['position'] = ",".join(te1)
                    self.class_plan.append(te)
        except CustomerError:
            # set kinds of errors and return different string
            # return str(e)
            return False
        # content = re.findall('var unitCount = 12;', self.text, re.DOTALL)
        # print(self.text)
        except:
            return False


if __name__ == '__main__':
    if len(sys.argv) == 4:
        obj = GetClassTable()
        obj.start_session()
        obj.login(sys.argv[1], sys.argv[2])
        obj.get_class(sys.argv[3])
        obj.stop_session()
        obj.parse_class()
        del obj
    else:
        pass
# class plan
# will add a profile in class to collect error message
