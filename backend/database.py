from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_Database ='sqlite:///./finance.db'

engine = create_engine(URL_Database,connect_args={'check_same_thread':False} )

sesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()