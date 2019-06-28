import requests
import json

#不带参数的get请求
# url="http://httpbin.org/get"
# res=requests.get(url)
# print(res.text)

# 带参数的get请求
# url1 = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好"  # 参数可以写到url里
# res1=requests.get(url=url1)
# print(res1.text)

#带参数的get请求，参数单独写出来
# url = "http://www.tuling123.com/openapi/api"
# params={"key":"ec961279f453459b9248f0aeb6600bbe","info":"你好"}
# res=requests.get(url=url,params=params)
# print(res.text)

# 传统表单类POST请求（x-www-form-urlencoded）
# url = "http://httpbin.org/post"
# data={"name":"hanzhichao","age":18}
# res=requests.post(url=url,data=data)
# print(res.text)

# JSON类型的POST请求（application/json）
# url = "http://httpbin.org/post"
# data="""{
# "name":"hanzhichao",
# "age":18
# }"""
# res=requests.post(url=url,data=data)
# print(res.text)

# 将data声明为字典格式
# import json
# url = "http://httpbin.org/post"
# data={
#     "name":"hanzhichao",
#     "age":18
# }
# headers={"Content-Type":"application/json"}#需要是headers
# res=requests.post(url=url,data=json.dumps(data),headers=headers)
# print(res.text)

# 将字典格式的data数据赋给post方法的json参数（可以自动将字典格式转为合法的JSON文本并添加headers）
# url = "http://openapi.tuling123.com/openapi/api/v2"
# data={
#     "reqType":0,
#     "perception":{
#         "inputText":{
#             "text":"附件的酒店"
#         },
#         "inputImage":{
#             "url":"imageUrl"
#         },
#         "selfInfo":{
#             "location":{
#                 "city":"北京",
#                 "province":"北京",
#                 "street":"回龙观东大街"
#             }
#         }
#     },
#     "userInfo":{
#         "apiKey":"ec961279f453459b9248f0aeb6600bbe",
#         "userId":"206379"
#     }
# }
# res=requests.post(url=url,json=data)
# print(res.text)

# json格式操作方法

# 序列化，转化为合法的json文本（方便http传输）
# import json
# data={"name":"张三","password":"123456","male":True,"money":None}
# str_data=json.dumps(data)
# print(str_data)

# json.dumps()支持将json文本格式化输出
# import json
# res = requests.post("http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=怎么又是你")
# print(res.text)
# res_dict=res.json()
# print(json.dumps(res_dict,indent=2,sort_keys=True,ensure_ascii=False))

# 反序列化
# res_text='''{"name": "\u5f20\u4e09", "password": "123456"}
# '''#json格式
# res_dict=json.loads(res_text)
# print(res_dict["name"])


# 文件的序列化
# 字典转化为文件句柄
# res_dict={'name': '张三', 'password': '123456', "male": True, "money": None} # 字典格式
# f=open("demo1.txt","w")
# json.dump(res_dict,f)

# 文件句柄转化为字典
# f=open("demo2.json","r",encoding="utf-8")
# f_dict=json.load(f)
# print(f_dict["name"])
# f.close()

# requests的使用方法
res = requests.get("https://www.baidu.com")
# print(res.status_code,res.reason)#200 OK
# print(res.text)#文本格式，有乱码
# print(res.content)#二进制格式
# print(res.encoding)# 查看解码格式 ISO-8859-1
# res.encoding='utf-8'#手动设置解密格式为“utf-8”
# print(res.text)#解决了乱码问题
# print(res.cookies.items)# cookies中的所有的项 [('BDORZ', '27315')]
# print(res.cookies.get("BDORZ")) # 获取cookies中BDORZ所对应的值 27315

# 带安全认证的请求
# 使用会话保持
# s=requests.session()
# s.post(url="https://demo.fastadmin.net/admin/index/login.html",data={"username":"admin","password":123456})
# res=s.get("https://demo.fastadmin.net/admin/dashboard?ref=addtabs")
# print(res.text)

# 抓取到的cookies然后写到代码中
url="https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
cookies={"PHPSESSID":"7e0711f7f6c929a4e5b237615dfd11b1"}
res=requests.get(url=url,cookies=cookies)
print(res.text)

