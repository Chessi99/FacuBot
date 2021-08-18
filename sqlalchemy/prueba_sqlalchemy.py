from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@127.0.0.1:3306/facubot')
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

Base = declarative_base()

class Materia(Base):
    __tablename__ = 'Materia'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255),unique=True)
    num_semestre = Column(Integer)

Base.metadata.create_all(engine) #-> Migra a la bd
materia = Materia(nombre="Ingenieria de software", num_semestre=6)
session.add(materia)
session.commit()

