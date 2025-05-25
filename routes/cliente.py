from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

cliente_route = Blueprint("cliente", __name__)

"""procurar cliente no banco de dados"""
@cliente_route.route('/')
def lista_clientes():
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)


"""inserir cliente no banco de dados"""
@cliente_route.route('/', methods=['POST'])
def inserir_clientes():

    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )

    return render_template('item_cliente.html', cliente=novo_usuario)


"""cadastro de um cliente"""
@cliente_route.route('/new')
def form_clientes():
    return render_template('form_clientes.html')


"""detalhes de um cliente"""
@cliente_route.route('/<int:cliente_id>')
def detalhe_clientes(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_clientes.html', cliente=cliente)


"""formulario para editar um cliente"""
@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_clientes(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_clientes.html', cliente = cliente)


"""atualizar informacao de um cliente"""
@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_clientes(cliente_id):
    #obter dados do formulario de edicao
    data = request.json
    #obter usuario pelo id
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()

    return render_template('item_cliente.html', cliente=cliente_editado)


"""deletar informacoes de um cliente"""
@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_clientes(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return{'deleted': 'ok'}

