from models.cpf import CPFModel
from marshmallow_sqlalchemy import  SQLAlchemyAutoSchema
from ma import ma

class CPFSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CPFModel
        load_instance = True