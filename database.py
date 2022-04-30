from singleton import Singleton
from contextlib import closing
import psycopg2

class Database(Singleton):
    def __init__(self, dbname, user, host="localhost"):
        self.__dbname = dbname
        self.__user = user
        self.__host = host

    def connect(self):
        return psycopg2.connect(dbname=self.__dbname, user=self.__user, host=self.__host)

    def execute(self, sql_query, conn):
        with closing(conn.cursor()) as cursor:
            cursor.execute(sql_query)
