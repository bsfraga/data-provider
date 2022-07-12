import logging

from flask import request
from flask_restx import Resource, Namespace, fields
from models.cpf import CPFModel
from services.four_devs import FourDevs

logging.basicConfig(level=logging.DEBUG, format=(
    '%(asctime)s : %(name)s : %(message)s'))

cpfdoc_ns = Namespace('cpf', description='CPF related operations')
cpfsdoc_ns = Namespace(
    'cpfs', description='CPFs related operations')

cpfdoc = cpfdoc_ns.model('CPF', {
    'cpf': fields.String(required=True, description='CPF'),
})
cpfsdoc = cpfsdoc_ns.model('CPFs', {
    'cpfs': fields.List(fields.Nested(cpfdoc))
})


class CPF(Resource):

    @cpfdoc_ns.doc('get cpf')
    @cpfdoc_ns.response(code=200, description='Success', model=cpfdoc)
    def get(self):
        resp = FourDevs().generate_cpf()
        if not resp or len(resp) == 0:
            return CPFModel.find_random(), 200
        cpf = CPFModel(resp)
        cpf.save()
        return cpf.json(), 200


class CPFs(Resource):

    @cpfsdoc_ns.doc('get cpfs')
    @cpfsdoc_ns.response(code=200, description='Success', model=cpfsdoc)
    def get(self):
        cpfs = CPFModel.query.all()
        return {'cpfs': [cpf.json() for cpf in cpfs]}, 200
