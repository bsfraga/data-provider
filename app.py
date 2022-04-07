from flask import Blueprint, Flask, jsonify
from flask_restx import Api
from marshmallow import ValidationError
from resources.company import Company, Companies, companydoc_ns, companiesdoc_ns
from resources.person import Person, Persons, persondoc_ns, personsdoc_ns
from resources.cpf import CPF, CPFs, cpfdoc_ns, cpfsdoc_ns
from resources.lorem_ipsum import LoremIpsum, loremdoc_ns
from resources.validations import ValidateCPF, ValidateCNPJ, ValidateCNH, ValidateCreditCardNumber, validationsdoc_ns
from sql_alchemy import db

app = Flask(__name__)

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/doc/', version='1.0', title='Data Provider',
          description='Data provider for test applications')

app.register_blueprint(blueprint)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_marshmallow_validation(e):
    return jsonify({'error': e.messages}), 400

api.add_namespace(companydoc_ns)
api.add_namespace(companiesdoc_ns)
api.add_namespace(persondoc_ns)
api.add_namespace(personsdoc_ns)
api.add_namespace(cpfdoc_ns)
api.add_namespace(cpfsdoc_ns)
api.add_namespace(loremdoc_ns)
api.add_namespace(validationsdoc_ns)


companydoc_ns.add_resource(Company, '', methods=['GET'])
companiesdoc_ns.add_resource(Companies, '', methods=['GET'])
persondoc_ns.add_resource(Person, '', methods=['GET'])
personsdoc_ns.add_resource(Persons, '', methods=['GET'])
cpfdoc_ns.add_resource(CPF, '', methods=['GET'])
cpfsdoc_ns.add_resource(CPFs, '', methods=['GET'])
loremdoc_ns.add_resource(LoremIpsum, '', methods=['GET'])

validationsdoc_ns.add_resource(ValidateCPF, '/cpf', methods=['GET'])
validationsdoc_ns.add_resource(ValidateCNPJ, '/cnpj', methods=['GET'])
validationsdoc_ns.add_resource(ValidateCNH, '/cnh', methods=['GET'])
validationsdoc_ns.add_resource(ValidateCreditCardNumber, '/credit_card_number', methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True)
