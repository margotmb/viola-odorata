import sqlite3
import os
from models.data import Data

class DBCrud:
    def __init__(self):
        self.__db_name = "url_shortener.db"

    @property
    def db_name(self):
        return self.__db_name

    def create_table(self):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_url TEXT NOT NULL,
        url_identifier TEXT NOT NULL
        )
        """)
        connection.commit()
        connection.close()

    def create_data(self, data: Data):
        connection = sqlite3.connect(self.__db_name)
        cur = connection.cursor()
        res_teste = cur.execute("SELECT * from data WHERE user_url LIKE ?", [data.user_url])
        if res_teste.fetchone() is None:
            cur.execute("INSERT INTO data (user_url, url_identifier) VALUES (?, ?)", (data.user_url, data.url_identifier))
            connection.commit()
            connection.close()
            return "DATA CREATED:" + str(data.user_url) + " -> " + str(data.url_identifier)
        else:
            connection.close()
            return "DATA ALREADY EXISTS"

    def read_url(self, data_string = None):
        connection = sqlite3.connect(self.__db_name)
        cur = connection.cursor()
        res = cur.execute("SELECT user_url from data WHERE url_identifier LIKE ?", [data_string])
        query = res.fetchone()
        connection.close()
        return query
