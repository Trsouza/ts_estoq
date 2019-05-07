from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from . import admin
from .forms import LoginForm, RegistrarForm, EditarUsuarioForm
from .. import db
from ..models import Usuario
from flask import Flask, request, jsonify
from ..decorators import admin_required

app = Flask(__name__) # removi isso nao fez diferença

@admin.route('/registrar', methods=['GET', 'POST'])
@login_required
@admin_required
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
        
        return redirect(url_for('admin.listar_usuarios'))
        
    return render_template('admin/usuario.html', registrar=True, form=form, title='Cadastrar-usuário')


@admin.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_usuario(id):

    usuario = Usuario.query.get_or_404(id)
    form = EditarUsuarioForm(obj=usuario)
 
    if form.validate_on_submit():
        usuario.nome_u = form.nome.data
        usuario.email_u = form.email.data
        usuario.senha = form.senha.data
        
        try:
            db.session.add(usuario)
            db.session.commit()
            flash('Usuario editado com sucesso.')
        except:
            flash('Erro')
        return redirect(url_for('admin.listar_usuarios'))

    form.nome.data = usuario.nome_u
    form.email.data = usuario.email_u
    form.senha.data = usuario.senha_u
    
    return render_template('admin/usuario.html',
                            registrar=False, form=form,
                            admin=admin, title="Editar Usuario")
                            
    #return redirect(url_for('admin.listar_usuarios'))


@admin.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def excluir_usuario(id):
    
    try:
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuario removido com sucesso.')
    except:
        flash('Erro ao remover o usuario')

    return redirect(url_for('admin.listar_usuarios'))

@admin.route('/usuarios', methods=['GET', 'POST'])
@login_required
def listar_usuarios():                             
    usuarios = Usuario.query.all()
    return render_template('admin/usuarios.html',
                           usuarios=usuarios, title="Usuarios")



# @admin.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():

#         usuario = Usuario.query.filter_by(email_u=form.email.data).first()
#         if usuario is not None and usuario.verify_password(form.senha.data):
#             login_user(usuario)
#             return redirect(url_for('main.dashboard'))
#         else:
#             flash('Email ou senha inválidos.')
#     return render_template('admin/login.html', form=form, title='Login')

# @admin.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('Desconectado')

#     return redirect(url_for('admin.login'))

