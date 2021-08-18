import pymysql.cursors


class DB(object):
    def __init__(self):
        self._db, self._connection = None, None
        self._new_connection()
    
    def _new_connection(self):
        if self._db is None or not self._db.connection:
            self._connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                database='facubot',
                                cursorclass=pymysql.cursors.DictCursor,
                                port=3306)
            self._db = self._connection.cursor()

    def execute(self,sql = None, *args):
        self._db.execute(sql,args)
        self._connection.commit()

    def execute_with_results(self,sql = None, *args):
        self._db.execute(sql, args)
        self._connection.commit()
        return self._db.fetchall()
