from bd.Database import DB

class Repository(object):
    def __init__(self):
        self._db = DB()

    def exists_subject(self, subject_name):
        query = 'SELECT * FROM `Materia` WHERE `nombre` = (%s)'
        result = self._db.execute_with_results(query, (subject_name,)) 
        return len(result) == 1

    def add_subject(self,subject_name, semester_number: int):
        query = 'INSERT INTO `Materia` (`nombre`,`num_semestre`) VALUES (%s,%s)'
        self._db.execute(query, subject_name, semester_number)

