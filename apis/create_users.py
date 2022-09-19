from configs.db_config import connect
from models.userModel import Base, User
from datetime import date
from fastapi import HTTPException

def insert_user(**kwargs):
    session = connect()
    new_user = User(
        name = kwargs.get('name'), 
        birthdate = kwargs.get('birthdate', None), 
        gender = kwargs.get('gender', None), 
        nationality = kwargs.get('nationality', None), 
        identity_id = kwargs.get('identity_id', None), 
        is_verify = kwargs.get('is_verify', False), 
        activated_phone = kwargs.get('activated_phone', None), 
        activated_email = kwargs.get('activated_email', None)
    )
    try:
        session.add(new_user)
        session.commit()
        session.close()
        return 
    except:
        session.rollback()
        session.close()
        raise HTTPException(status_code=400)

