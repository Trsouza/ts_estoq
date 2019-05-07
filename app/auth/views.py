from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from . import auth
from .forms import LoginForm, RegistrarForm
from .. import db
from ..models import Usuario
from flask import Flask, request, jsonify

app = Flask(__name__) # removi isso nao fez diferença

@auth.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrarForm()
        
    if form.validate_on_submit():
        usuario = Usuario(  nome_u=form.nome.data,
                            email_u=form.email.data,
                            senha=form.senha.data                            
                            )
        db.session.add(usuario)
        db.session.commit()
        flash('Registro efetuado com sucesso.')
        
        return redirect(url_for('auth.inicio'))
        
    return render_template('auth/registrar.html', registrar=True, form=form, title='Cadastrar-usuário')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        usuario = Usuario.query.filter_by(email_u=form.email.data).first()
        if usuario is not None and usuario.verify_password(form.senha.data):
            login_user(usuario)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Email ou senha inválidos.')
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Desconectado')

    return redirect(url_for('auth.login'))

@auth.route('/inicio')
@login_required
def inicio():
    return render_template('main/index.html', title="Painel de Controle")
