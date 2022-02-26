import json
import logging

from flask import request
from flask_restx import Namespace, Resource, fields
from services.four_devs import FourDevs

logging.basicConfig(level=logging.DEBUG, format=(
    '%(asctime)s : %(name)s : %(message)s'))

loremdoc_ns = Namespace('lorem_ipsum', description='Lorem Ipsum generator')

loremdoc = loremdoc_ns.model('LoremIpsum', {
    'content': fields.String(description='Lorem Ipsum content'),
})

loremdoc_error = loremdoc_ns.model('LoremIpsumError', {
    'message': fields.String(description='Error message'),
})


class LoremIpsum(Resource):

    @loremdoc_ns.doc('generate lorem ipsum')
    @loremdoc_ns.response(code=200, description='Success', model=loremdoc)
    @loremdoc_ns.response(code=500, description='Internal Server Error', model=loremdoc_error)
    @loremdoc_ns.response(code=400, description='Bad Request', model=loremdoc_error)
    @loremdoc_ns.param('quantity', 'Quantity of paragraphs or words', required=True, _in='header')
    @loremdoc_ns.param('options', 'Options: paragraphs or words', required=True, options=['paragraphs', 'words'], _in='header')
    def get(self):
        if request.headers.get('options') is None or request.headers.get('quantity') is None or request.headers.get('options') != 'words' and request.headers.get('options') != 'paragraphs':
            return {'message' : 'Bad Request'}, 400
        resp = FourDevs().generate_lorem_ipsum(quantity=request.headers.get(
            'quantity'), options=request.headers.get('options'))
        if not resp:
            return {'message' : 'Internal Server Error'}, 500

        return {'content': resp[1:-1]}, 200
