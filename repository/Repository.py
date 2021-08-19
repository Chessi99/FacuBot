from models.models import *
from .SessionSingleton import SessionSingleton

class Repository(object):
    def __init__(self):
        self._session = SessionSingleton.singleton().session

    def retrieve_subject(self,subject_name):
        return self._session.query(Subject).filter(Subject.name == subject_name).first()
   
    def exists_subject(self, subject_name):
        # result = self._session.query(Subject).filter(Subject.name == subject_name).all()
        return self.retrieve_subject(subject_name) is not None

    def add_subject(self,subject_name, semester_number: int):
        subject = Subject(name = subject_name, semester_number = semester_number)
        self._session.add(subject)
        self._session.commit()

    def update_subject(self,subject_name):
        pass

    def delete_subject(self,subject_name):
        pass    

