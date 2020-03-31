import requests
import ast


token_dic = requests.get("https://v2.jinrishici.com/token")
token = ast.literal_eval(token_dic.text)
token_dic.close()
header = {"X-User-Token": token["data"]}
sentence = requests.get("https://v2.jinrishici.com/sentence", headers=header)
print(sentence.text)
# poem is an dictionary of data, use print to know how to use it
sentence.close()
# need to parse json to what we need
# 此为每日一词的接口，调用方法为以上，建议重构时按照获取课程表的try-except方式构建，毕竟是其他人的api出错也没法修复
