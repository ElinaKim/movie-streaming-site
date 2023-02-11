from flask import Flask, jsonify, request
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
    name = CharField(unique = True)
    def to_dict(self):
        return{
            'name': self.name
        }

class Movie(BaseModel):
    title = CharField(unique = True)
    def to_dict(self):
        return{
            'id': self.id,
            'title': self.title
        }

class MovieActor(BaseModel):
    actor_id = ForeignKeyField(Actor)
    movie_id = ForeignKeyField(Movie)


@app.route('/')
def index():
    return 'Hello World.'


@app.route('/api/movies', methods = ['GET'])
def get_movies():
    with db.connection_context():
        movies = Movie.select()
        return jsonify({'movies': [movie.to_dict() for movie in movies.execute()]}), 200


@app.route('/api/movies/<id>', methods = ['GET'])
def get_movie(id):
    with db.connection_context():
        movie = Movie.get(Movie.id == id)
    return {'name': movie.title}, 200


@app.route('/api/movies', methods = ['POST'])
def create_movie():
    movie = request.json
    name = movie['name']
    with db.connection_context():
        Movie.create(title = name)
    return {'movie':f'{name} was created'}, 201
        

@app.route('/api/movies/<id>', methods = ['PUT'])
def update_movie(id):
    movie = request.json 
    name = movie['name']
    with db.connection_context():
        Movie.update(title = name).where(Movie.id == id).execute()
    return {'movie': f'{name} was updated'}, 200


@app.route('/api/movies/<int:id>', methods = ['DELETE'])
def delete_movie(id):
    with db.connection_context():
        Movie.delete().where(Movie.id == int(id)).execute()
    return jsonify({'message': f'Movie with id {id} was deleted.'}), 200

if __name__ == '__main__':
    app.run()