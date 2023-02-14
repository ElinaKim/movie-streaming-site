from db.models.baseModel import BaseModel
from peewee import CharField

class Actor(BaseModel):
    name = CharField(unique = True)
    def to_dict(self):
        return{
            'name': self.name
        }