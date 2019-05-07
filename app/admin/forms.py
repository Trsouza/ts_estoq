from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Regexp
from flask import flash
from ..models import Usuario
import re

class RegistrarForm(FlaskForm):
   
    nome = StringField('Nome', validators=[DataRequired(),
                                             Regexp('^[A-Za-z \s]+$', 0,
										'Campo nome permitido apenas letras')                                              
                                                 ])
   
    email = StringField('Email', validators=[DataRequired(), Email()
										# ,Regexp('[A-Za-z0-9\\._-]+@([a][l][u]\.)?[u][f][c]\.[b][r]', 0,
										# 'Email inválido ')
										])                                                 
    senha = PasswordField('Senha', validators=[
                                        DataRequired()
                                            #Regexp('^([A-Za-z0-9]{8,})+$', 0,
   										# ,Regexp('^([A-Za-z0-9]{8,})$', 0,
										# 'Senha deve ser composta de no mínimo 8 dígitos sendo eles letras e números '),
                                        ,EqualTo('confirme_senha', message = 'As senhas devem ser iguais')
                                        ])
    confirme_senha= PasswordField('Repita a senha')                                        
    
    submit = SubmitField('Salvar')

    def validate_email(self, field):
        if Usuario.query.filter_by(email_u=field.data).first():
            raise ValidationError('Email já cadastrado.')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class EditarUsuarioForm(FlaskForm):
   
    nome = StringField('Nome', validators=[DataRequired(),
                                             Regexp('^[A-Za-z \s]+$', 0,
										'Campo nome permitido apenas letras')                                              
                                        ])
    
    email = StringField('Email', validators=[DataRequired(), Email()
										# ,Regexp('[A-Za-z0-9\\._-]+@([a][l][u]\.)?[u][f][c]\.[b][r]', 0,
										# 'Email inválido ')
										])                                                 
    senha = PasswordField('Senha', validators=[
                                        DataRequired()
                                            #Regexp('^([A-Za-z0-9]{8,})+$', 0,
   										# ,Regexp('^([A-Za-z0-9]{8,})$', 0,
										# 'Senha deve ser composta de no mínimo 8 dígitos sendo eles letras e números '),
                                        ,EqualTo('confirme_senha')
                                        ])
    confirme_senha= PasswordField('Repita a senha')
    
    submit = SubmitField('Atualizar')