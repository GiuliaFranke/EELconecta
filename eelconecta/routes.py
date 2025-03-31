#criar as rotas do nosso site

from flask import render_template, url_for, request, jsonify
from eelconecta import app
from eelconecta.materias import disciplinas_eletrica, disciplinas_eletronica, disponiveis, recomendacao

#caminho dos links
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eletrica')
def eletrica():
    return render_template('eletrica.html')

@app.route('/eletronica')
def eletronica():
    return render_template('eletronica.html')

@app.route('/api/check_subjects', methods=['POST'])
def check_subjects():
    data = request.json
    selected = data.get('selected', [])
    course = data.get('course', 'eletrica')
    
    # Seleciona o dicionário correto de disciplinas
    disciplinas = disciplinas_eletrica if course == 'eletrica' else disciplinas_eletronica
    
    # Calcula disciplinas disponíveis
    available = disponiveis(selected)
    
    return jsonify({
        'available': available,
        'recommended': recomendacao(available)
    })