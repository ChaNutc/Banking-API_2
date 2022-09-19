from utils.history import request_statement
from utils.find_account import find_account

def retrive_history(account):
    find_account(account) # find account is in db
    statement = request_statement(account)
    return statement
