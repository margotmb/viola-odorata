import sqlite3
from models.data import Data
import re


class DBConnector:
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
        regex_result = re.search("^http*", data.user_url)
        if (regex_result is None):
            data.user_url = "https://" + data.user_url
        connection = sqlite3.connect(self.__db_name)
        cur = connection.cursor()
        cur.execute("INSERT INTO data (user_url, url_identifier) VALUES (?, ?)",
                    (data.user_url, data.url_identifier))
        connection.commit()
        connection.close()
        return "DATA CREATED:" + str(data.user_url) + " -> " + str(data.url_identifier)

    def read_url(self, data_string=None):
        connection = sqlite3.connect(self.__db_name)
        cur = connection.cursor()
        res = cur.execute(
            "SELECT user_url from data WHERE url_identifier LIKE ?", [data_string])
        query = res.fetchone()
        connection.close()
        return query
