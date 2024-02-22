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
        print("TABLE CREATED")
        connection.close()

    
    def create_data(self, data: Data):
        connection = sqlite3.connect(self.__db_name)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO data (user_url, url_identifier) VALUES (?, ?)", (data.user_url, data.url_identifier))
        connection.commit()
        print("DATA CREATED:" + str(data.user_url) + " -> " + str(data.url_identifier) )
        connection.close()
