from sqlalchemy import Column, String, Integer, Numeric, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'

    account_number = Column(String, primary_key=True)
    user_id = Column(Integer)
    bank = Column(String)
    balance = Column(Numeric)

    def __init__(self, account_number, user_id, bank, balance):
        self.account_number = account_number
        self.user_id = user_id
        self.bank = bank
        self.balance = balance
