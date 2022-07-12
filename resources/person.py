import logging
import json
from flask import request
from flask_restx import Resource, Namespace, fields
from models.person import PersonModel
from services.four_devs import FourDevs
from schemas.person import PersonSchema

logging.basicConfig(level=logging.DEBUG, format=(
    '%(asctime)s : %(name)s : %(message)s'))

persondoc_ns = Namespace('person', description='Person related operations')
personsdoc_ns = Namespace(
    'persons', description='Persons related operations')

person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)

persondoc = persondoc_ns.model('Person', {
    'nome': fields.String(required=True, description='Person name'),
    'idade': fields.Integer(required=True, description='Person age'),
    'cpf': fields.String(required=True, description='Person cpf'),
    'rg': fields.String(required=True, description='Person rg'),
    'data_nasc': fields.String(required=True, description='Person data_nasc'),
    'sexo': fields.String(required=True, description='Person sexo'),
    'signo': fields.String(required=True, description='Person signo'),
    'mae': fields.String(required=True, description='Person mae'),
    'pai': fields.String(required=True, description='Person pai'),
    'email': fields.String(required=True, description='Person email'),
    'senha': fields.String(required=True, description='Person senha'),
    'cep': fields.String(required=True, description='Person cep'),
    'endereco': fields.String(required=True, description='Person endereco'),
    'numero': fields.String(required=True, description='Person numero'),
    'bairro': fields.String(required=True, description='Person bairro'),
    'cidade': fields.String(required=True, description='Person cidade'),
    'estado': fields.String(required=True, description='Person estado'),
    'telefone_fixo': fields.String(required=True, description='Person telefone_fixo'),
    'celular': fields.String(required=True, description='Person celular'),
    'altura': fields.String(required=True, description='Person altura'),
    'peso': fields.String(required=True, description='Person peso'),
    'tipo_sanguineo': fields.String(required=True, description='Person tipo_sanguineo'),
    'cor': fields.String(required=True, description='Person color'),
})
personsdoc = personsdoc_ns.model('Persons', {
    'persons': fields.List(fields.Nested(persondoc))
})

class Person(Resource):

    @persondoc_ns.doc('get person')
    @persondoc_ns.response(code=200, description='Success', model=persondoc)
    def get(self):
        resp = FourDevs().generate_person()
        if not resp or len(resp) == 0:
            return PersonModel.find_random(), 200
        person = PersonModel(**resp[0])  
        person.save()
        return person_schema.dump(person), 200


class Persons(Resource):

    @personsdoc_ns.doc('get persons')
    @personsdoc_ns.response(code=200, description='Success', model=personsdoc)
    def get(self):
        persons = PersonModel.query.all()
        return {'persons': persons_schema.dump(persons)}, 200