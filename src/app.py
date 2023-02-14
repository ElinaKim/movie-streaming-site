from flask import Flask
from db.repositories.actor import ActorRepository
from db.repositories.movie import MovieRepository

app = Flask(__name__)

movieRepo = MovieRepository()
actorRepo = ActorRepository()


@app.route('/')
def index():
    return 'Hello World.'

@app.route('/api/movies', methods = ['GET'])
def get_movies():
    return movieRepo.getAllMovies


@app.route('/api/movies/<id>', methods = ['GET'])
def get_movie(id):
    return movieRepo.getMovie(id)


@app.route('/api/movies', methods = ['POST'])
def create_movie():
    return movieRepo.addMovie()
        

@app.route('/api/movies/<id>', methods = ['PUT'])
def update_movie(id):
    return movieRepo.updateMovie(id)


@app.route('/api/movies/<int:id>', methods = ['DELETE'])
def delete_movie(id):
    return movieRepo.deleteMovie(id)


@app.route('/api/actors', methods = ['GET'])
def get_actors():
    return actorRepo.getAllActors()

@app.route('/api/actors/<id>', methods = ['GET'])
def get_actor(id):
    return actorRepo.getActor(id)

@app.route('/api/actors', methods = ['POST'])
def create_actor():
    return actorRepo.addActor()
        
@app.route('/api/actors/<id>', methods = ['PUT'])
def update_actor(id):
    return actorRepo.updateActor(id)

@app.route('/api/actors/<int:id>', methods = ['DELETE'])
def delete_actor(id):
    return actorRepo.deleteActor(id)


# @app.route('/api/movie_actors', methods = ['GET'])
# def get_actors_by_movie():
#     with db.connection_context():
#         query = (Movie
#         .select(Movie.title.alias('movie_title'), Actor.name.alias('actor_name'))
#         .join(MovieActor, on = (MovieActor.movie_id == Movie.id))
#         .join(Actor, on = (MovieActor.actor_id == Actor.id)))
#     results = [{'movie_title': movie.movie_title, 'actor_name': movie.actor.actor_name} for movie in query]
#     return results

if __name__ == '__main__':
    app.run()