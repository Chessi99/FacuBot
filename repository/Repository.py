from models.models import *
from .SessionSingleton import SessionSingleton

class Repository(object):
    def __init__(self):
        self._session = SessionSingleton.singleton().session

    def exists_subject(self, subject_name):
        result = self._session.query(Subject).filter(Subject.name == subject_name).all()
        print(result)
        return False
        #query = 'SELECT * FROM `Materia` WHERE `nombre` = (%s)'
        #result = self._db.execute_with_results(query, (subject_name,)) 
        #return len(result) == 1

    def add_subject(self,subject_name, semester_number: int):
        subject = Subject(name = subject_name, semester_number = semester_number)
        self._session.add(subject)
        self._session.commit()

