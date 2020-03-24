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