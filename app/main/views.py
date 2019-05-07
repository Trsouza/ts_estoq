from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from . import main
#from .forms import 
from .. import db
from ..models import  Usuario
    
@main.route('/')
def index():
    return render_template('main/index.html', title="Bem Vindo")

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html', title="Painel de Controle")

