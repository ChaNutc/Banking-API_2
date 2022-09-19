from fastapi import HTTPException
from utils.generate_transaction_id import generate_uuid
from utils.update_account_balance import make_transaction

def deposit_transaction(**kwargs):
    
    uuid = kwargs.get('uuid', generate_uuid())
    
    origin_account = kwargs.get('origin_account')
    destination_account = kwargs.get('destination_account', None)
    channel = kwargs.get('channel') # iOS, Android, Web
    transaction_name = 'deposit'
    indicator = 'C'
    amount = kwargs.get('amount')
    description = kwargs.get('description', None)
    parent_id = kwargs.get('parent_id', None) # related uuid

    if amount <= 0:
        raise HTTPException(status_code=400)

    make_transaction(
        uuid = uuid, 
        origin_account = origin_account, 
        destination_account = destination_account, 
        channel = channel, 
        transaction_name = transaction_name, 
        indicator = indicator, 
        amount = amount, 
        description = description, 
        parent_id = parent_id
        )