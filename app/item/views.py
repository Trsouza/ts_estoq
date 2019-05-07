from flask import abort, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required
from . import item
from .forms import CriarItemForm, EditarItemFormEntrada, EditarItemFormSaida #, VisualizarForm
from .. import db
from ..models import Item, Usuario

# from datetime import date
# data_atual = date.today()

@item.route('/itens', methods=['GET', 'POST'])
@login_required
def listar_itens():                             
    itens = Item.query.all()
    return render_template('item/itens.html',
                           itens=itens, title="Itens")
 

@item.route('/add', methods=['GET', 'POST'])
@login_required
def add_item():
    
    form = CriarItemForm()
    
    if form.validate_on_submit():
        item =  Item(nome_i=form.nome.data, quantidade_i=form.quantidade.data)
        try:
            db.session.add(item)
            db.session.commit()
            flash('Item cadastrado com sucesso.')
        except:
            flash('Erro: Já existe um produto com esse nome.')

        return redirect(url_for('item.listar_itens'))
    return render_template('item/item.html',
                            add_item=True, form=form,
                            title="Cadastrar Item")
    #return redirect(url_for('item.listar_itens'))

@item.route('/edit/entrada<int:id>', methods=['GET', 'POST'])
@login_required
def editar_item_entrada(id):

    item = Item.query.get_or_404(id)
    form = EditarItemFormEntrada(obj=item)
 
    if form.validate_on_submit():
        item.nome_i = form.nome.data

        item.quantidade_i = int (form.quantidade.data) + int (form.entrada.data)
       
        # flash(item.quantidade_i )
        try:
            db.session.add(item)
            db.session.commit()
            flash('Item editado com sucesso.')
        except:
            flash('Erro: Já existe um produto com esse nome.')
        return redirect(url_for('item.listar_itens'))

    form.quantidade.data = item.quantidade_i
    form.nome.data = item.nome_i
    
    return render_template('item/item.html',
                            add_item=False, form=form,
                            item=item, title="Editar Item")

@item.route('/edit/saida/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_item_saida(id):

    item = Item.query.get_or_404(id)
    form = EditarItemFormSaida(obj=item)
 
    if form.validate_on_submit():
        item.nome_i = form.nome.data

        item.quantidade_i = int (form.quantidade.data) -  int (form.saida.data)
       
        # flash(item.quantidade_i )
        try:
            db.session.add(item)
            db.session.commit()
            flash('Item editado com sucesso.')
        except:
            flash('Erro: Já existe um produto com esse nome.')
        return redirect(url_for('item.listar_itens'))

    form.quantidade.data = item.quantidade_i
    form.nome.data = item.nome_i
    
    return render_template('item/item.html',
                            add_item=False, form=form,
                            item=item, title="Editar Item")
    

# @item.route('/<int:id>', methods=['GET', 'POST'])
# @login_required
# def visualizar_item(id):

#     item = Item.query.get_or_404(id)
#     form = VisualizarForm(obj=item)

#     form.quantidade.data = item.quantidade_i
#     form.nome.data = item.nome_i
#     return render_template('item/item.html',
#                            form=form,
#                            item=item, title="Visualizar Item")

@item.route('/excluir/<int:id>', methods=['GET', 'POST'])
@login_required
def excluir_item(id):
    
    try:
        item = Item.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        flash('Item removido com sucesso.')
    except:
        flash('Erro ao remover o item')

    return redirect(url_for('item.listar_itens'))
    

