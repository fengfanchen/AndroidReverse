import time

from application import app, manager
from flask_script import Command, Server
from common.dbOperator import DBOperator
from common.httpOperator import PhoneHttp
from common.phoneOperator import PhoneOperator

manager.add_command("runserver",Server( host = "0.0.0.0",use_debugger=True,use_reloader= True ))


@Command
def autoReg():
    httpPhone = PhoneHttp()
    httpPhone.login()
    dbOper = DBOperator()
    phone = PhoneOperator(dbOper, httpPhone)

    for i in range(0, 50):

        try:
            phone.run()
        except Exception as e:
            import traceback
            traceback.print_exc()

        phone.closeApp()
        time.sleep(5)

    pass


manager.add_command("autoReg", autoReg)


def main():
    manager.run()

if __name__ == "__main__":
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()