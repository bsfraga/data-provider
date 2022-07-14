from sql_alchemy import db


class PersonModel(db.Model):

    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    rg = db.Column(db.String(20), nullable=False)
    data_nasc = db.Column(db.String(10), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    signo = db.Column(db.String(20), nullable=False)
    mae = db.Column(db.String(100), nullable=False)
    pai = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    telefone_fixo = db.Column(db.String(20), nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    altura = db.Column(db.String(10), nullable=False)
    peso = db.Column(db.String(10), nullable=False)
    tipo_sanguineo = db.Column(db.String(2), nullable=False)
    cor = db.Column(db.String(20), nullable=False)

    def __init__(self, nome, idade, cpf, rg, data_nasc, sexo, signo, mae, pai, email, senha, cep, endereco, numero, bairro, cidade, estado, telefone_fixo, celular, altura, peso, tipo_sanguineo, cor):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.signo = signo
        self.mae = mae
        self.pai = pai
        self.email = email
        self.senha = senha
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.telefone_fixo = telefone_fixo
        self.celular = celular
        self.altura = altura
        self.peso = peso
        self.tipo_sanguineo = tipo_sanguineo
        self.cor = cor

    def json(self):
        return {
            'nome': self.nome,
            'idade': self.idade,
            'cpf': self.cpf,
            'rg': self.rg,
            'data_nasc': self.data_nasc,
            'sexo': self.sexo,
            'signo': self.signo,
            'mae': self.mae,
            'pai': self.pai,
            'email': self.email,
            'senha': self.senha,
            'cep': self.cep,
            'endereco': self.endereco,
            'numero': self.numero,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'estado': self.estado,
            'telefone_fixo': self.telefone_fixo,
            'celular': self.celular,
            'altura': self.altura,
            'peso': self.peso,
            'tipo_sanguineo': self.tipo_sanguineo
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_random(cls):
        return cls.query.order_by(db.func.random()).first().json()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def delete(cls, nome):
        cls.query.filter_by(nome=nome).delete()
        db.session.commit()
