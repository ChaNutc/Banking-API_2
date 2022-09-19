import random
from datetime import datetime
from models.accountModel import Account

def generate_bank_account(session):
    account = [a.account_number for a in session.query(Account).all()]
    return str(generate(account))

def generate(account):
    random.seed(int(datetime.now().utcnow().timestamp()))
    random_account = random.randint(1111111111,9999999999)
    # check exists
    if random_account in account:
        generate(account)
    else:
        return random_account