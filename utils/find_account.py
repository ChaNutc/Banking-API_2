from models.accountModel import Account
from configs.db_config import connect
from fastapi import HTTPException

def find_account(account_number):
    # Find if have account in db, will return account and raise error 404 if not founded.
    session = connect()
    try:
        res = session.query(Account).filter(Account.account_number == account_number).first().account_number
        session.close()
        return res
    except:
        session.close()
        raise HTTPException(status_code=404,detail='Account not found')
    