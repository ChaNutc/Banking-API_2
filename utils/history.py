from fastapi import HTTPException
from models.transactionModel import Base, Transaction
from configs.db_config import connect

def request_statement(account):
    session = connect()
    # return history
    try:
        res = session.query(Transaction).filter(Transaction.account_number == account).all()
        session.close()
        return res
    except:
        session.close()
        raise HTTPException(status_code=500)