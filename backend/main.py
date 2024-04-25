from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dbcrud import DBCrud
from models.data import Data
from models.req_data import ReqData
import random
import string

# Connector object
con = DBCrud()

# Generate Tables
con.create_table()

data = Data(user_url="https://google.com", url_identifier="abcde")
con.create_data(data)


def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters)
                         for i in range(length))
    return result_str


# FastAPI -> 'uvicorn main:app --reload' to run local server
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title> Homepage </title>
        </head>
        <body>
            <h1> Homepage </h1>
        </body>
    </html>

"""


@app.get("/{url_id}")
def read(url_id):
    query = con.read_url(url_id)
    if query:
        return RedirectResponse(query[0])
    else:
        return None


@app.post("/create_url_id/")
def create_url_id(req: ReqData):
    print(req.user_url)
    url_id = get_random_string(8)
    res = con.create_data(Data(user_url=req.user_url, url_identifier=url_id))
    print(res)
    return JSONResponse({"url_id": url_id})
