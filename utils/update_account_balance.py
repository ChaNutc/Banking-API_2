from models.accountModel import Account
from fastapi import HTTPException
from models.transactionModel import Base, Transaction
from datetime import datetime
from configs.db_config import connect

def make_transaction(**kwargs):
    #log transaction
    session = connect()

    uuid = kwargs.get('uuid')
    origin_account = kwargs.get('origin_account')
    destination_account = kwargs.get('destination_account', None)
    channel = kwargs.get('channel') # iOS, Android, Web
    transaction_name = kwargs.get('transaction_name') # deposit, withdraw
    indicator = kwargs.get('indicator') # Credit, Debit
    amount = kwargs.get('amount')
    description = kwargs.get('description', None)
    parent_id = kwargs.get('parent_id', None) # related uuid
    timestamp = datetime.now()

    # update balance in account
    update_balance(session, origin_account, amount)

    # insert new transaction log
    trans = Transaction(
        transaction_id = uuid, 
        datetime = timestamp, 
        account_number = origin_account, 
        transaction_account = destination_account, 
        channel = channel,
        transaction_name = transaction_name,
        indicator = indicator,
        amount = amount,
        description = description,
        parent_id = parent_id
    )
    try:
        session.add(trans)
        session.commit()
        session.close()
        return 
    except:
        session.rollback()
        session.close()
        raise HTTPException(status_code=400)

def update_balance(session, account_number, amount):
    # update balance in account
    session.query(Account).filter(Account.account_number == account_number).\
        update({Account.balance:amount+Account.balance}, synchronize_session = False)