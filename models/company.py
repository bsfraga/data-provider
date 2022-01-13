from sql_alchemy import db


class CompanyModel(db.Model):

    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    inscricao_estadual = db.Column(db.String(20), nullable=False)
    data_abertura = db.Column(db.String(10), nullable=False)
    site = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cep = db.Column(db.String(10), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    telefone_fixo = db.Column(db.String(20), nullable=False)
    celular = db.Column(db.String(20), nullable=False)

    def __init__(self, nome, cnpj, inscricao_estadual, data_abertura, site, email, cep, endereco, numero, cidade, bairro, estado, telefone_fixo, celular):
        self.nome = nome
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.data_abertura = data_abertura
        self.site = site
        self.email = email
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.cidade = cidade
        self.bairro = bairro
        self.estado = estado
        self.telefone_fixo = telefone_fixo
        self.celular = celular

    def json(self):
        return {
            'nome': self.nome,
            'cnpj': self.cnpj,
            'inscricao_estadual': self.inscricao_estadual,
            'data_abertura': self.data_abertura,
            'site': self.site,
            'email': self.email,
            'cep': self.cep,
            'endereco': self.endereco,
            'numero': self.numero,
            'cidade': self.cidade,
            'bairro': self.bairro,
            'estado': self.estado,
            'telefone_fixo': self.telefone_fixo,
            'celular': self.celular
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_random(cls):
        return cls.query.order_by(db.func.random()).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
