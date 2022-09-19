from configs.db_config import connect
from models.accountModel import Base, Account
from utils.generate_bank_account import generate_bank_account
from apis.deposit_transactions import deposit_transaction
from fastapi import HTTPException

def create_bankaccount(user_id, bank, channel, amount):
    if amount < 500 :
        raise HTTPException(status_code=400)
    session = connect()
    bank_account = generate_bank_account(session)

    account = Account(
        account_number = bank_account, 
        user_id = user_id, 
        bank = bank, 
        balance = 0
    )
    try:
        session.add(account)
        session.commit()
        session.close()
    except:
        session.rollback()
        session.close()
        raise HTTPException(status_code=400)
    deposit_transaction(
                    origin_account = bank_account, 
                    channel = channel, 
                    amount = amount,
                    description = "Open an account.")
