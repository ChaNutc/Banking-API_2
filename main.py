from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi
import uvicorn
from pydantic import BaseModel
import decimal
from apis.create_users import insert_user
from apis.create_bank_accounts import create_bankaccount
from apis.deposit_transactions import deposit_transaction
from apis.withdraw_transactions import withdraw_transaction
from apis.transfer_transactions import transfer_transaction
from apis.retrive_balance import balance
from apis.retrive_histories import retrive_history

app = FastAPI()

class Userpayload(BaseModel):
    name:str

class Accountpayload(BaseModel):
    user_id:int
    bank:str 
    amount:decimal.Decimal
    channel:str

class Depositpayload(BaseModel):
    account_number:str
    amount:decimal.Decimal
    channel:str

class Withdrawpayload(BaseModel):
    account_number:str
    amount:decimal.Decimal
    channel:str

class Transferpayload(BaseModel):
    origin_account:str
    destination_account:str
    amount:decimal.Decimal
    channel:str

class Balancepayload(BaseModel):
    account_number:str

class Historypayload(BaseModel):
    account_number:str

@app.post("/api/create_user", status_code=200)
async def create_user(payload:Userpayload):
    res = insert_user( name = payload.name )

@app.post("/api/open_account", status_code=200)
async def open_account(payload:Accountpayload):
    create_bankaccount( user_id=payload.user_id, 
                        bank=payload.bank, 
                        amount=payload.amount, 
                        channel=payload.channel
                        )

@app.post("/api/deposit", status_code=200)
async def deposit(payload:Depositpayload):
    deposit_transaction( origin_account=payload.account_number,
                        channel=payload.channel,
                        amount=payload.amount
                        )

@app.post("/api/withdraw", status_code=200)
async def withdraw(payload:Withdrawpayload):
    withdraw_transaction( origin_account=payload.account_number,
                        channel=payload.channel,
                        amount=payload.amount
                        )

@app.post("/api/transfer", status_code=200)
async def transfer(payload:Transferpayload):
    transfer_transaction( origin_account=payload.origin_account, 
                            destination_account=payload.destination_account,
                            channel=payload.channel,
                            amount=payload.amount
                            )

@app.post("/api/retrive_balance", status_code=200)
async def retrive_balance(payload:Balancepayload):
    account, acc_balance, timestamp = balance( payload.account_number )
    return {
        "account" : account,
        "balance" : acc_balance,
        "timestamp" : timestamp
    }

@app.post("/api/retrive_histories")
async def history(payload:Historypayload):
    return retrive_history(payload.account_number)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")