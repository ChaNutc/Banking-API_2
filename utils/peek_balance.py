from models.accountModel import Account
from configs.db_config import connect

def peek_balance(account_number):
    session = connect()
    # return balance
    try:
        res = session.query(Account).filter(Account.account_number == account_number).first().balance
        session.close()
        return res
    except:
        session.close()
        raise HTTPException(status_code=500)