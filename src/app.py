from flask import Flask 
import peewee
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
conn_str = os.getenv("CONN_STR") 

database = peewee.PostgresqlDatabase(conn_str)  

@app.route('/')
def index():
    return 'Hello World.'

if __name__ == '__main__':
    app.run()