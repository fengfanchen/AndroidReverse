import requests
import time
import json

class PhoneHttp():
    def __init__(self):
        self.session = requests.session()
        self.url = {
            "loginUrl" : "http://api.xxxxxxxxxx.com/sms/?api=login&user=用户名&pass=密码",
            "getPhoneUrl" : " http://api.xxxxxxxxxx.com/sms/?api=getPhone&token=登录时返回的令牌&sid=项目ID",
            "getMessageUrl": "http://api.xxxxxxxxxx.com/sms/?api=getMessage&token=登陆返回的令牌&sid=项目ID&phone=取到的手机号码",
            "cancelAllRecvUrl": "http://api.xxxxxxxxxx.com/sms/?api=cancelAllRecv&token=登陆返回的令牌"
        }
        self.userToken = ""
        self.projectId = 666666
        self.userName = "qq666666666"
        self.password = "qq666666666"
        self.phone = ""
        pass

    #登录
    def login(self):
        url = self.url['loginUrl'].replace("用户名", self.userName).replace("密码", self.password)
        content = self.handleRequest("GET", url)
        print("登录url:" + url)
        retJson = {}

        while True:
            content = self.handleRequest("GET", url)
            if len(retJson) < 200:
                retJson = json.loads(content)
                break
            else:
                print("登录 时 辣鸡服务器出现500")
                time.sleep(10)

        self.userToken = retJson["token"]
        if retJson["msg"] == "success":
            print("login success")
            print(retJson)
            return True

        return False

    #获取手机号
    def getPhone(self):
        url = self.url['getPhoneUrl'].replace("登录时返回的令牌", self.userToken).replace("项目ID", str(self.projectId))
        retJson = {}
        while True:
            content = self.handleRequest("GET", url)
            if len(retJson) < 200:
                retJson = json.loads(content)
                break
            else:
                print("获取手机号 时 辣鸡服务器出现500")
                time.sleep(10)

        if retJson["msg"] == "success":
            self.phone = retJson["phone"]
            return retJson["phone"]
        return "0"

    #获取验证码
    def getMessage(self):
        url = self.url['getMessageUrl'].replace("登陆返回的令牌", self.userToken).replace("项目ID", str(self.projectId)).replace("取到的手机号码", self.phone)

        for i in range(1, 10):
            content = self.handleRequest("GET", url)
            if len(content) > 100:
                time.sleep(10)
                continue
            print("content:" + content)
            retJson = json.loads(content)
            print("the url is " + url)
            print("have get message " + str(i) + " time")
            if retJson["code"] == '-1':
                time.sleep(5)
            else:
                #释放手机号，返回验证码
                self.phone = ""
                releaseUrl = self.url['cancelAllRecvUrl'].replace("登录时返回的令牌", self.userToken)
                self.handleRequest("GET", releaseUrl)
                print(retJson)
                return retJson['yzm']

        #超时返回0,释放手机号
        releaseUrl = self.url['cancelAllRecvUrl'].replace("登录时返回的令牌", self.userToken)
        self.handleRequest("GET", releaseUrl)
        return "0"

    def handleRequest(self, method, url, data = None, head = None, info = None):

        try:
            if method == "GET":
                response = self.session.get(url, headers=head, timeout=60)
                pass
            elif method == "POST":
                response = self.post(url, headers=head, timeout=60, data=data)
                pass
        except IOError:
            return None

        return response.text


