from fastapi import HTTPException
from utils.generate_transaction_id import generate_uuid
from utils.find_account import find_account
from apis.deposit_transactions import deposit_transaction
from apis.withdraw_transactions import withdraw_transaction

def transfer_transaction(**kwargs):
    
    uuid = generate_uuid()

    origin_account = kwargs.get('origin_account')
    destination_account = kwargs.get('destination_account')
    channel = kwargs.get('channel') # iOS, Android, Web
    amount = kwargs.get('amount')
    description = kwargs.get('description', None)
    parent_id = kwargs.get('parent_id', None) # related uuid

    if origin_account == destination_account: 
        # Cannot transfer to same account
        raise HTTPException(status_code=400)

    find_account(destination_account)# find account is in db

    withdraw = withdraw_transaction(
                    uuid = uuid, 
                    origin_account = origin_account, 
                    destination_account = destination_account, 
                    channel = channel, 
                    amount = amount,
                    description = description,
                    parent_id = parent_id
                    )
    deposit = deposit_transaction(
                    origin_account = destination_account, 
                    destination_account = origin_account, 
                    channel = channel, 
                    amount = amount,
                    description = description,
                    parent_id = uuid
                    )