from repository.Repository import Repository

class Service(object):
    def __init__(self):
        self.repository = Repository()

    def add_subject(self, subject_name, semester_number):
        if not self.repository.exists_subject(subject_name):
            self.repository.add_subject(subject_name, semester_number)
            return True
        return False






    