from db.models.baseModel import BaseModel
from peewee import CharField

class Movie(BaseModel):
    title = CharField(unique = True)
    def to_dict(self):
        return{
            'id': self.id,
            'title': self.title
        }
