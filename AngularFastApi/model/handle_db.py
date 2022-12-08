import sqlite3
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class HandleDB():
    def __init__(self):
        try:
        # self._con = sqlite3.connect("./users.db")
        # self._cur = self._con.cursor()
        
            self._con = psycopg2.connect(
                                            host="localhost",
                                            port="5432",
                                            database="fastApiDB",
                                            user="fastperson",
                                            password="fastperson")
            #psycopg2.connect("dbname=fastApiDB user=fastperson password=fastperson host=localhost port=5432")
            self._cur = self._con.cursor()
        except psycopg2.OperationalError as error:
            print(error)
            self._con.close()

    def get_all(self):
        self._cur.execute("SELECT * FROM users")
        data=self._cur.fetchall()
        return data

    def get_only(self, data_user):
        self._cur.execute("SELECT * FROM users WHERE username = '{}'".format(data_user))
        data=self._cur.fetchone()
        return data

    def insert(self,data_user):
        self._cur.execute("INSERT INTO users VALUES('{}','{}','{}','{}','{}','{}')".format(
            data_user["id"],
            data_user["firstname"],
            data_user['lastname'],
            data_user['username'],
            data_user['country'],
            data_user['password_user']
        ))
        self._con.commit()
        

    def __del__(self):
        self._con.close()

