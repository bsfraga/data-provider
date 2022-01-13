from sql_alchemy import db

class CPFModel(db.Model):

    __tablename__ = 'cpf'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(14), nullable=False)

    def __init__(self, cpf):
        self.cpf = cpf

    def json(self):
        return {
            'cpf': self.cpf
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