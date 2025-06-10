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
    recommended = recomendacao(available, course)
    
    return jsonify({
        'available': available,
        'recommended': recommended
    })
