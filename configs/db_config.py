# import psycopg2
from fastapi import HTTPException
import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect():
    load_dotenv()

    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_PORT = os.getenv('DB_PORT')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    
    try:
        engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        Session = sessionmaker(bind=engine)
        return Session()
    except:
        raise HTTPException(status_code=500,detail='Postgres connection error')


# def postgresConnection(): #config file for creat connection to postgres
#     load_dotenv()

#     DB_HOST = os.getenv('DB_HOST')
#     DB_NAME = os.getenv('DB_NAME')
#     DB_PORT = os.getenv('DB_PORT')
#     DB_USERNAME = os.getenv('DB_USERNAME')
#     DB_PASSWORD = os.getenv('DB_PASSWORD')
    
#     try:
#         conn = psycopg2.connect(
#             host=DB_HOST,
#             database=DB_NAME,
#             port=DB_PORT,
#             user=DB_USERNAME,
#             password=DB_PASSWORD
#         )
#         return conn
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Error: %s" % error)
#         raise HTTPException(status_code=500,detail='Postgres connection error')