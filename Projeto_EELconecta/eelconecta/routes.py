from flask import render_template, url_for, request, jsonify
from eelconecta import app
from eelconecta.recomendadas import recomendacao
from eelconecta.disciplinas_disponiveis import disponiveis

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

    available = disponiveis(selected, course)

    return jsonify({
        'available': available
    })

@app.route('/recomendadas', methods=['POST'])
def recomendadas():
    data = request.json
    selecionadas = data.get('selecionadas', [])
    curso = data.get('curso', 'eletrica')
    valor_slider = data.get('valor_slider', 15)

    # Importante: chamar a função recomendacao que deve estar implementada
    recomendadas = recomendacao(selecionadas, curso, valor_slider)

    return jsonify({
        'recomendadas': recomendadas
    })
