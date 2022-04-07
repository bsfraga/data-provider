import logging

from flask import request
from flask_restx import Namespace, Resource, fields
from services.four_devs import FourDevs
import re


logging.basicConfig(level=logging.DEBUG, format=(
    '%(asctime)s : %(name)s : %(message)s'))


validationsdoc_ns = Namespace('validations', description='Validations')

valid_documents_doc = validationsdoc_ns.model('CPF', {
    'valid': fields.Boolean(description='True if valid False if not.'),
})


error_doc = validationsdoc_ns.model('Error', {
    'message': fields.String(description='Error message'),
})

bad_doc = validationsdoc_ns.model('Bad Request', {
    'message': fields.String(description='Bad Request message'),
})


class ValidateCPF(Resource):

    @validationsdoc_ns.doc('Validate CPF')
    @validationsdoc_ns.response(code=200, description='Success', model=valid_documents_doc)
    @validationsdoc_ns.response(code=500, description='Internal Server Error', model=error_doc)
    @validationsdoc_ns.response(code=400, description='Bad Request', model=bad_doc)
    @validationsdoc_ns.param('cpf', 'CPF to be validated', required=True, _in='header')
    def get(self):
        if request.headers.get('cpf') is None:
            return {'message' : 'Bad Request'}, 400

        if not re.match(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', request.headers.get('cpf')):
            return {'message' : 'Bad Request'}, 400

        resp = FourDevs().validate_cpf(request.headers.get('cpf'))
        return {'valid': resp}, 200


class ValidateCNPJ(Resource):

    @validationsdoc_ns.doc('Validate CNPJ')
    @validationsdoc_ns.response(code=200, description='Success', model=valid_documents_doc)
    @validationsdoc_ns.response(code=500, description='Internal Server Error', model=error_doc)
    @validationsdoc_ns.response(code=400, description='Bad Request', model=bad_doc)
    @validationsdoc_ns.param('cnpj', 'CNPJ to be validated', required=True, _in='header')
    def get(self):
        if request.headers.get('cnpj') is None:
            return {'message' : 'Bad Request'}, 400

        if not re.match(r'^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$', request.headers.get('cnpj')):
            return {'message' : 'Bad Request'}, 400

        resp = FourDevs().validate_cnpj(request.headers.get('cnpj'))
        return {'valid': resp}, 200

class ValidateCNH(Resource):

    @validationsdoc_ns.doc('Validate CNH')
    @validationsdoc_ns.response(code=200, description='Success', model=valid_documents_doc)
    @validationsdoc_ns.response(code=500, description='Internal Server Error', model=error_doc)
    @validationsdoc_ns.response(code=400, description='Bad Request', model=bad_doc)
    @validationsdoc_ns.param('cnh', 'CNH to be validated', required=True, _in='header')
    def get(self):
        if request.headers.get('cnh') is None:
            return {'message' : 'Bad Request'}, 400

        if len(request.headers.get('cnh')) != 11:
            return {'message' : 'Bad Request'}, 400

        resp = FourDevs().validate_cnh(request.headers.get('cnh'))
        return {'valid': resp}, 200

class ValidateCreditCardNumber(Resource):

    @validationsdoc_ns.doc('Validate Credit Card Number')
    @validationsdoc_ns.response(code=200, description='Success', model=valid_documents_doc)
    @validationsdoc_ns.response(code=500, description='Internal Server Error', model=error_doc)
    @validationsdoc_ns.response(code=400, description='Bad Request', model=bad_doc)
    @validationsdoc_ns.param('credit_card_number', 'Credit Card Number to be validated', required=True, _in='header')
    @validationsdoc_ns.param('flag', 'Credit Card Flag', required=True, _in='header', 
    enum=['Visa', 'MasterCard', 'Visa Electron', 'American Express', 'Diners Club', 'Discover', 'Enroute', 'JCB', 'Maestro', 'Solo', 'Switch', 'LaserCard'])
    def get(self):
        if request.headers.get('flag') is None:
            return {'message' : 'Bad Request'}, 400

        if request.headers.get('credit_card_number') is None:
            return {'message' : 'Bad Request'}, 400

        if len(request.headers.get('credit_card_number')) > 20:
            return {'message' : 'Bad Request'}, 400

        resp = FourDevs().validate_credit_card_number(request.headers.get('credit_card_number'), request.headers.get('flag'))
        return {'valid': resp}, 200