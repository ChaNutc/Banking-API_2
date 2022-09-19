from utils.peek_balance import peek_balance
from fastapi import HTTPException
from datetime import datetime
from utils.find_account import find_account

def balance(account_number):
    find_account(account) # find account is in db
    timestamp = datetime.now()
    acc_balance = peek_balance(account_number)
    return account_number, acc_balance, timestamp