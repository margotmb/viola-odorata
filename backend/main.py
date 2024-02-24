from fastapi import FastAPI
from fastapi.responses import FileResponse
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

@app.get("/{url_id}/")
def read(url_id):
    #returns tuple
    query = con.read_url(url_id)
    return query[0]