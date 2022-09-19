from fastapi import HTTPException
from utils.generate_transaction_id import generate_uuid
from utils.peek_balance import peek_balance
from utils.update_account_balance import make_transaction

def withdraw_transaction(**kwargs):
    uuid = kwargs.get('uuid', generate_uuid())

    origin_account = kwargs.get('origin_account')
    destination_account = kwargs.get('destination_account', None)
    channel = kwargs.get('channel') # iOS, Android, Web
    transaction_name = 'withdraw'
    indicator = 'D'
    amount = kwargs.get('amount')
    description = kwargs.get('description', None)
    parent_id = kwargs.get('parent_id', None) # related uuid

    balance = peek_balance(origin_account) # Peek balance to check user withdraw amount

    if amount <= 0:
        # check amount cannot minus value
        session.close()
        raise HTTPException(status_code=400)
    if balance + (amount * -1) < 0:
        # check withdraw cannot more than balance
        session.close()
        raise HTTPException(status_code=400)

    make_transaction(
        uuid = uuid, 
        origin_account = origin_account, 
        destination_account = destination_account, 
        channel = channel, 
        transaction_name = transaction_name, 
        indicator = indicator, 
        amount = (amount * -1), 
        description = description, 
        parent_id = parent_id
        )