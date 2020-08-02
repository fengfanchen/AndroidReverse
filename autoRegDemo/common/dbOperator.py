from application import db
from common.models.account import Account

class DBOperator():
    def __init__(self):
        pass

    def setAccountAndPassword(self, account, password):

        newAccount = {}
        newAccount['userName'] = account
        newAccount['password'] = password
        accountModel = Account(**newAccount)
        db.session.add(accountModel)
        db.session.commit()

        pass
    pass
