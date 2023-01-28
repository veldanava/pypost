# py post for ctf
import requests as req
url = "http://165.227.106.113/post.php"
data = {"username":"<censored>","password":"<censored>"}
res = req.post(url , data=data)
print(res.status_code)
print(res.text)