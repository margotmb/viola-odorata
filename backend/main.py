import sqlite3
import os
from fastapi import FastAPI

# Checks if DB didn't exist prior to connection/creation
db_exists = os.path.exists("tutorial.db")

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

if not db_exists:
    print("Creating Tables")
    cur.execute("CREATE TABLE shortener(link, shortened_id)")

res = cur.execute("SELECT link FROM shortener")

#fetchall -> Returns entire query as a list, each item as tuple
queryAsList = res.fetchall()
print(queryAsList)

# Test FastAPI -> 'uvicorn main:app --reload' to run server
app = FastAPI()

@app.get("/")
def read_root():
    return "Test_Run"