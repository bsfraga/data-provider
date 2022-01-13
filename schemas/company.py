from models.company import CompanyModel
from marshmallow_sqlalchemy import  SQLAlchemyAutoSchema
from ma import ma

class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CompanyModel
        load_instance = True