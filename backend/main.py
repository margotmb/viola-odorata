from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dbcrud import DBCrud
from models.data import Data
import random
import string

#Connector object
con = DBCrud()

#Generate Tables
con.create_table()

data = Data(user_url = "https://google.com", url_identifier = "abcde")
con.create_data(data)

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str

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


@app.post("/create_url_id/")
def create_url_id(user_url):
    url_id = get_random_string(8)
    res = con.create_data(Data(user_url = user_url, url_identifier = url_id))
    print(res)
    return "localhost:8000/"+ url_id