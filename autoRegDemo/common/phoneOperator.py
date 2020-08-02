import uiautomator2 as u2
# from common.dbOperator import DBOperator
# from common.httpOperator import PhoneHttp

class PhoneOperator(object):
    def __init__(self, dbOper, httpOper, serial="6e0bc87e"):
        self.d = u2.connect_usb(serial=serial)
        self.dbOper = dbOper
        self.httpOper = httpOper
        self.password = "dafadsfafasdfdsaf"
        pass


    def closeApp(self):
        self.d.app_stop('com.xxxxx.yyyyy')
        pass

    def run(self):
        self.d.app_start('com.xxxxx.yyyyy')
        startBack = self.d(resourceId="com.xxxxx.yyyyy:id/s_", text="以后提醒").exists(timeout=20)
        if startBack:
            self.d(resourceId="com.xxxxx.yyyyy:id/s_", text="以后提醒").click()
            self.getInviteCode()
            pass
        else:
            pass
        pass

    def getInviteCode(self):
        self.d(resourceId="com.xxxxx.yyyyy:id/h3").click()
        self.d(resourceId="com.xxxxx.yyyyy:id/wb", text="分享推广").click()
        inviteCode = self.d(resourceId="com.xxxxx.yyyyy:id/vb").get_text()
        print("邀请码为：" + inviteCode)
        self.d.press("back")
        self.d(resourceId="com.xxxxx.yyyyy:id/w5", text="切换账号").click()
        self.d(resourceId="com.xxxxx.yyyyy:id/ta", text="注册").click()

        #获取手机号
        phoneNum = self.httpOper.getPhone()
        print(phoneNum)
        if phoneNum != "0":
            self.d(resourceId="com.xxxxx.yyyyy:id/c8", text="请输入您的手机号码").set_text(phoneNum)
            self.d(resourceId="com.xxxxx.yyyyy:id/b6", text="获取验证码").click()

            #查看下号码能不能用 等待2s
            s59 = self.d(resourceId="com.xxxxx.yyyyy:id/b6", text="59秒后重试").exists(timeout=3)
            if not s59:
                print("这个号码有问题，重新开始")
                return


            msg = self.httpOper.getMessage()
            if msg != "0":

                #已经获取了验证码
                self.d(resourceId="com.xxxxx.yyyyy:id/c9", text="请输入验证码").set_text(msg)
                self.d.press("back")
                self.d(resourceId="com.xxxxx.yyyyy:id/ca", text="请输入密码").set_text(self.password)
                self.d.press("back")
                self.d(resourceId="com.xxxxx.yyyyy:id/c_", text="请再次输入密码").set_text(self.password)
                self.d.press("back")
                self.d(resourceId="com.xxxxx.yyyyy:id/b7", text="确定").click()

                #绑定邀请码
                self.d(resourceId="com.xxxxx.yyyyy:id/wb", text="分享推广").click()
                self.d(resourceId="com.xxxxx.yyyyy:id/cb", text="输入对方推广码").set_text(inviteCode)
                self.d(resourceId="com.xxxxx.yyyyy:id/b8", text="绑定").click()
                self.d.press("back")

                #记录到数据库
                self.dbOper.setAccountAndPassword(phoneNum, self.password)
            else:
                print("获得了手机号，但没有验证码，已释放")
                return
        else:
           print("没有获去手机号")

        pass