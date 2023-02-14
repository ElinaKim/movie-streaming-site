import os 
from dotenv import load_dotenv 
import peewee

load_dotenv()

conn_str = os.getenv("CONN_STR") 

db = peewee.PostgresqlDatabase(conn_str) 
