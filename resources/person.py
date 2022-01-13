import logging
import json
from flask import request
from flask_restx import Resource, Namespace, fields
from models.person import PersonModel
from services.four_devs import FourDevs

logging.basicConfig(level=logging.DEBUG, format=(
    '%(asctime)s : %(name)s : %(message)s'))

persondoc_ns = Namespace('person', description='Person related operations')
personsdoc_ns = Namespace(
    'persons', description='Persons related operations')

persondoc = persondoc_ns.model('Person', {})
personsdoc = personsdoc_ns.model('Persons', {
    'persons': fields.List(fields.Nested(persondoc))
})

class Person(Resource):

    @persondoc_ns.doc('get person')
    @persondoc_ns.response(code=200, description='Success', model=persondoc)
    def get(self):
        resp = FourDevs().generate_person()
        if not resp:
            return PersonModel.find_random(), 200
        person = PersonModel(**resp)  
        person.save()
        return person.json(), 200


class Persons(Resource):

    @personsdoc_ns.doc('get persons')
    @personsdoc_ns.response(code=200, description='Success', model=personsdoc)
    def get(self):
        persons = PersonModel.query.all()
        return {'persons': [person.json() for person in persons]}, 200