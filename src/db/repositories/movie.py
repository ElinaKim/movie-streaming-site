from db.connection import db
from db.models import Movie
from flask import jsonify, request

class MovieRepository:
    def getAllMovies(self):
        with db.connection_context():
            movies = Movie.select()
        return jsonify({'movies': [movie.to_dict() for movie in movies.execute()]}), 200

    def getMovie(self, id):
        with db.connection_context():
            movie = Movie.get(Movie.id == id)
        return {'name': movie.title}, 200
    
    def addMovie(self):
        movie = request.json
        movie_name = movie['name']
        with db.connection_context():
            Movie.create(title = movie_name)
        return {'movie':f'{movie_name} was created'}, 201
    
    def updateMovie(self, id):
        movie = request.json 
        name = movie['name']
        with db.connection_context():
            Movie.update(title = name).where(Movie.id == id).execute()
        return {'movie': f'{name} was updated'}, 200

    def deleteMovie(self, id):
        with db.connection_context():
            Movie.delete().where(Movie.id == int(id)).execute()
        return jsonify({'message': f'Movie with id {id} was deleted.'}), 200


