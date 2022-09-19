from sqlalchemy import Column, String, DateTime, Numeric, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(String, primary_key=True)
    datetime = Column(DateTime)
    account_number = Column(String)
    transaction_account = Column(String)
    channel = Column(String)
    transaction_name = Column(String)
    indicator = Column(String)
    amount = Column(Numeric)
    description = Column(String)
    parent_id = Column(String)

    def __init__(self, transaction_id, datetime, account_number, transaction_account, channel, transaction_name, indicator, amount, description, parent_id):
        self.transaction_id = transaction_id
        self.datetime = datetime
        self.account_number = account_number
        self.transaction_account = transaction_account
        self.channel = channel
        self.transaction_name = transaction_name
        self.indicator = indicator
        self.amount = amount
        self.description = description
        self.parent_id = parent_id
