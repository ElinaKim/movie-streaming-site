from db.connection import db
from db.models import Actor
from flask import jsonify, request

class ActorRepository:
    def getAllActors(self):
        with db.connection_context():
            actors = Actor.select()
        return jsonify({'actors': [actor.to_dict() for actor in actors.execute()]}), 200

    def getActor(self, id):
        with db.connection_context():
            actor = Actor.get(Actor.id == id)
        return {'name': actor.name}, 200
    
    def addActor(self):
        actor = request.json
        actor_name = actor['name']
        with db.connection_context():
            Actor.create(name = actor_name)
        return {'actor':f'{actor_name} was created'}, 201
    
    def updateActor(self, id):
        actor = request.json 
        actor_name = actor['name']
        with db.connection_context():
            Actor.update(name = actor_name).where(Actor.id == id).execute()
        return {'movie': f'{actor_name} was updated'}, 200

    def deleteActor(self, id):
        with db.connection_context():
            Actor.delete().where(Actor.id == int(id)).execute()
        return jsonify({'message': f'Actor with id {id} was deleted.'}), 200

    
    
