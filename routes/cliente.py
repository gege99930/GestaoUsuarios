from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint("cliente", __name__)

"""procurar cliente no banco de dados"""
@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)


"""inserir cliente no banco de dados"""
@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
    data = request.json
    novo_usuario = {
        "id": len(CLIENTES)+1,
        "nome": data['nome'],
        "email": data['email'],
    }
    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)


"""cadastro de um cliente"""
@cliente_route.route('/new')
def form_clientes():
    return render_template('form_clientes.html')


"""detalhes de um cliente"""
@cliente_route.route('/<int:cliente_id>')
def detalhe_clientes(cliente_id):
    return render_template('detalhe_clientes.html')


"""formulario para editar um cliente"""
@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_clientes(cliente_id):
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
    return render_template('form_clientes.html', cliente = cliente)


"""atualizar informacao de um cliente"""
@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_clientes(cliente_id):
    pass


"""deletar informacoes de um cliente"""
@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_clientes(cliente_id):
    global CLIENTES
    CLIENTES=[ c for c in CLIENTES if c['id'] != cliente_id ]
    return{'deletd': 'ok'}

