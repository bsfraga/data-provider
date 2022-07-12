import logging

from flask import request
from flask_restx import Resource, Namespace, fields
from models.company import CompanyModel
from services.four_devs import FourDevs
from utils.bs4_parser import BeautifulSoupParser

logging.basicConfig(level=logging.DEBUG, format=(
    '%(asctime)s : %(name)s : %(message)s'))

companydoc_ns = Namespace('company', description='Company related operations')
companiesdoc_ns = Namespace(
    'companies', description='Companies related operations')

companydoc = companydoc_ns.model('Company', {
    'nome': fields.String(required=True, description='Company name'),
    'cnpj': fields.String(required=True, description='Company cnpj'),
    'endereco': fields.String(required=True, description='Company endereco'),
    'numero': fields.String(required=True, description='Company numero'),
    'bairro': fields.String(required=True, description='Company bairro'),
    'cidade': fields.String(required=True, description='Company cidade'),
    'estado': fields.String(required=True, description='Company estado'),
    'cep': fields.String(required=True, description='Company cep'),
    'telefone_fixo': fields.String(required=True, description='Company telefone_fixo'),
    'celular': fields.String(required=True, description='Company celular'),
    'email': fields.String(required=True, description='Company email'),
    'site': fields.String(required=True, description='Company site'),
    'inscricao_estadual': fields.String(required=True, description='Company inscricao_estadual'),
    'data_abertura': fields.String(required=True, description='Company data_abertura'),
})
companiesdoc = companiesdoc_ns.model('Companies', {
    'companies': fields.List(fields.Nested(companydoc))
})


class Company(Resource):

    @companydoc_ns.doc('get company')
    @companydoc_ns.response(code=200, description='Success', model=companydoc)
    def get(self):
        resp = FourDevs().generate_company()
        content = BeautifulSoupParser.parseHtml(resp)
        if not content or len(content) == 0:
            return CompanyModel.find_random(), 200
        company = CompanyModel(**content)  
        company.save()
        return company.json(), 200


class Companies(Resource):

    @companiesdoc_ns.doc('get companies')
    @companiesdoc_ns.response(code=200, description='Success', model=companiesdoc)
    def get(self):
        companies = CompanyModel.query.all()
        return {'companies': [company.json() for company in companies]}, 200