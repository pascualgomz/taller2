from flask import Blueprint, jsonify, render_template
import random
import socket
from .models import POKENEAS

main = Blueprint('main', __name__)

@main.route('/api/pokenea', methods=['GET'])
def get_pokenea():
    pokenea = random.choice(POKENEAS)
    response = {
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        'contenedor_id': socket.gethostname()
    }
    return jsonify(response)

@main.route('/pokenea', methods=['GET'])
def show_pokenea():
    pokenea = random.choice(POKENEAS)
    return render_template('pokenea.html', pokenea=pokenea, contenedor_id=socket.gethostname())
