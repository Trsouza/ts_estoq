from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Regexp
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Item, Usuario


class CriarItemForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(),
                                             Regexp('^[A-Za-z0-9 \s]+$', 0,
										'Campo nome permitido apenas letras e números')                                              
                                                 ])
    quantidade = StringField('Quantidade', validators=[DataRequired(),
                                             Regexp('^[0-9 \s]+$', 0,
										'Campo quantidade permitido apenas números')                                              
                                                 ])

    cadastrar = SubmitField('Salvar')

    #
    def validate_nome(self, field):
        if Item.query.filter_by(nome_i=field.data).first():
            raise ValidationError('Item já cadastrado.')

class EditarItemFormEntrada(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(),
                                             Regexp('^[A-Za-z0-9 \s]+$', 0,
										'Campo nome permitido apenas letras e números')                                              
                                                 ])
    quantidade = StringField('Quantidade', validators=[DataRequired(),
                                             Regexp('^[0-9 \s]+$', 0,
										'Campo quantidade permitido apenas números')                                              
                                                 ])
    entrada = StringField('Entrada', validators=[
                                             Regexp('[0-9 \s]+$', 0,
										'Campo quantidade permitido apenas números')                                              
                                                 ])
                                                                                                
    cadastrar = SubmitField('Salvar')

class EditarItemFormSaida(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(),
                                             Regexp('^[A-Za-z0-9 \s]+$', 0,
										'Campo nome permitido apenas letras e números')                                              
                                                 ])
    quantidade = StringField('Quantidade', validators=[DataRequired(),
                                             Regexp('^[0-9 \s]+$', 0,
										'Campo quantidade permitido apenas números')                                              
                                                 ])
    saida = StringField('Saída', validators=[
                                             Regexp('[0-9 \s]+$', 0,
										'Campo quantidade permitido apenas números')                                              
                                                 ])                                                                                                 
    cadastrar = SubmitField('Salvar')

class BuscarItem(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(),
                                             Regexp('^[A-Za-z0-9 \s]+$', 0,
										'Campo nome permitido apenas letras e números')                                              
                                                 ])
    buscar = SubmitField('Buscar')                                                

# class VisualizarForm(FlaskForm):
#     nome = StringField('Nome', validators=[DataRequired()])
#     quantidade = StringField('Quantidade', validators=[DataRequired()])
#     entrada = StringField('Entrada', validators=[DataRequired()])
    #saida = StringField('Saída', validators=[DataRequired()])