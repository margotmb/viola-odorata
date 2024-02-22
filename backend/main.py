from fastapi import FastAPI
from dbcrud import DBCrud
from models.data import Data
import sqlite3

#Connector object
con = DBCrud()

#Generate Tables
con.create_table()

data = Data(user_url = "url_test", url_identifier = "identificador_teste")
con.create_data(data)

#FastAPI -> 'uvicorn main:app --reload' to run server
app = FastAPI()

@app.get("/db_url/")
def read():
    connection = sqlite3.connect(con.db_name)
    cur = connection.cursor()
    res = cur.execute("SELECT * FROM data")
    queryAsList = res.fetchall()
    connection.close()
    return queryAsList