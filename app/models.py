from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager
from datetime import date, datetime
from flask_login import current_user
from pytz import timezone

               

class Relatorio(db.Model):
   
    __tablename__ = 'relatorios'

    id_r = db.Column(db.Integer, primary_key=True)
    data_r = db.Column(db.DateTime, default=datetime.utcnow)
    quantidade_r = db.Column(db.Integer)
    id_user_fk = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    id_item_fk = db.Column(db.Integer, db.ForeignKey('itens.id_i'))
    
    def __init__(self, data_r, quantidade_r, id_user_fk, id_prod_fk):
        self.data_r = data_r
        self.quantidade_r = quantidade_r
        self.id_user_fk = id_user_fk
        self.id_prod_fk = id_prod_fk    

class Item(db.Model):
       
    fuso_horario = timezone('America/Sao_Paulo')

    __tablename__ = 'itens'

    id_i = db.Column(db.Integer, primary_key=True)
    nome_i = db.Column(db.String(100))
    quantidade_i = db.Column(db.Integer)
    data_i =  db.Column(db.Date, default=date.today, onupdate=date.today)

    relatorio_i = db.relationship('Relatorio', foreign_keys=[Relatorio.id_item_fk], 
                              backref=db.backref('relatorioI',lazy='joined'),lazy='dynamic', 
                              cascade='all, delete-orphan')

    def __init__(self, nome_i, quantidade_i): 
        self.nome_i = nome_i
        self.quantidade_i = quantidade_i

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome_u = db.Column(db.String(100))
    email_u = db.Column(db.String(50))
    senha_u = db.Column(db.String(200))
    tipo_user = db.Column(db.Boolean, default=True) 

    relatorio_u = db.relationship('Relatorio', foreign_keys=[Relatorio.id_user_fk], 
                              backref=db.backref('relatorioU',lazy='joined'),lazy='dynamic', 
                              cascade='all, delete-orphan')

    @property
    def senha(self):
        raise AttributeError('senha não é um atributo legível, models...')

    @senha.setter # impossibilita ler a senha
    def senha(self, senha):
        self.senha_u = generate_password_hash(senha)

    def verify_password(self, senha):
        return check_password_hash(self.senha_u, senha)

    #def __repr__(self):
    #    return '<Usuario: {}>'.format(self.username)         

               
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

