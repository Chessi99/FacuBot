from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class SessionSingleton(object):
    instance = None
    
    @classmethod
    def singleton(className):
        if not className.instance:
            engine = create_engine('mysql://root:root@127.0.0.1:3306/facubot') #TODO pasar los datos al .env
            Session = sessionmaker()
            Session.configure(bind=engine)
            className.instance = SessionSingleton(Session(),engine)
        return className.instance

    def __init__(self,session, engine):
        self.session = session
        self.engine = engine

    

