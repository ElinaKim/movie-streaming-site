from flask import Flask 
from peewee import *
import peewee
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
conn_str = os.getenv("CONN_STR") 

db = peewee.PostgresqlDatabase(conn_str)  

class BaseModel(Model):
    class Meta:
        database = db

class Actor(BaseModel):
    name = CharField(50)


class Movie(BaseModel):
    actor_id = ForeignKeyField(Actor, backref = 'actor_id')
    title = CharField(50)
    year = IntegerField
    time = IntegerField


@app.route('/')
def index():
    return 'Hello World.'

db.connect()
db.create_tables([Actor, Movie])

if __name__ == '__main__':
    app.run()