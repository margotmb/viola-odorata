from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dbcrud import DBCrud
from models.data import Data
import sqlite3

#Connector object
con = DBCrud()

#Generate Tables
con.create_table()

data = Data(user_url = "https://google.com", url_identifier = "abcde")
con.create_data(data)

#FastAPI -> 'uvicorn main:app --reload' to run server
app = FastAPI()

@app.get("/")
def home():
    return "Homepage"

@app.get("/{url_id}/")
def read(url_id):
    #returns tuple
    query = con.read_url(url_id)
    
    if query:
        return RedirectResponse(query[0])
    else:
        return None


@app.post("/create_url_id/{user_url}")
def create_url_id(user_url):
    return ""