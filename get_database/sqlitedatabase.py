import sqlite3


def load_db():
    conn = sqlite3.connect("./db/database.db")
    cursor = conn.cursor()
    try:
        cursor.execute("select * from classplan")
        values = cursor.fetchall()
        print(values)
    except:
        cursor.execute("create table classplan(cname varchar(50),position varchar(3),week varchar(53),pname varchar(50))")
    finally:
        conn.close()
def getclass(index):
    s = ""
    for i in range(int(index)):
        s = s + "_"
    s = s + "1%"
    conn = sqlite3.connect("./db/database.db")
    try:
        cursor = conn.cursor()
        cursor.execute("select * from classplan where week like '%s'"%s)
        values = cursor.fetchall()
        return values
    except:
        print("error")
        return []
    finally:
        conn.close()


def add_item(cname, position, week, pname):
    conn = sqlite3.connect("./db/database.db")
    flag = 0
    try:
        cursor = conn.cursor()
        cursor.execute("insert into classplan values('%s','%s','%s','%s')"%(cname,position,week,pname))
        conn.commit()
        flag = 1
    except:
        print("error")
        flag = 0
    finally:
        conn.close()
        if flag == 1:
            return True
        else:
            return False


def delete_item(cname):
    conn = sqlite3.connect("./db/database.db")
    flag = 0
    try:
        cursor = conn.cursor()
        cursor.execute("delete from classplan where cname = '%s'"%cname)
        conn.commit()
        flag = 1
    except:
        print("error")
        flag = 0
    finally:
        conn.close()
        if flag == 1:
            return True
        else:
            return False
