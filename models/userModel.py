from sqlalchemy import Column, String, Integer, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthdate = Column(Date)
    gender = Column(String)
    nationality = Column(String)
    identity_id = Column(String)
    is_verify = Column(Boolean)
    activated_phone = Column(String)
    activated_email = Column(String)

    def __init__(self, name, birthdate, gender, nationality, identity_id, is_verify, activated_phone, activated_email):
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.nationality = nationality
        self.identity_id = identity_id
        self.is_verify = is_verify
        self.activated_phone = activated_phone
        self.activated_email = activated_email
