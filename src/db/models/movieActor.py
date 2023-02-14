from peewee import ForeignKeyField

from db.models import Actor, Movie

from .baseModel import BaseModel

class MovieActor(BaseModel):
    actor_id = ForeignKeyField(Actor, backref = 'movies')
    movie_id = ForeignKeyField(Movie, backref = 'actors')