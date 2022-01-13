from models.person import PersonModel
from marshmallow_sqlalchemy import  SQLAlchemyAutoSchema
from ma import ma

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PersonModel
        load_instance = True