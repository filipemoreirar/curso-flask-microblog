from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    name = "Filipe M"
    age = 30
    data = {"profissao": "Analista",
            "sexo": "Masculino"}
    
    return render_template('index.html', nome = name, dados = data, idade=age)

@app.route('/contato')
def contato():
    return render_template('contato.html')
