from repository.Repository import Repository

class Service(object):
    def __init__(self):
        self.repository = Repository()

    def add_subject(self, subject_name, semester_number):
        if self.repository.exists_subject(subject_name):
            return False
        self.repository.add_subject(subject_name, semester_number)
        return True

    def delete_subject(self,subject_name):
        if not self.repository.exists_subject(subject_name):
            return False
        self.repository.delete_subject(subject_name)
        return True

    def update_subject(self,old_subject_name,new_subject_name):
        if not self.repository.exists_subject(old_subject_name) or self.repository.exists_subject(new_subject_name):
            return False
        self.repository.update_subject(subject_name)
        return True

    