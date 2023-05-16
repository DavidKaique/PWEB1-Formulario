from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return "Página Inicial"

@app.route ('/novaconta')
def novaconta ():
    return render_template('cadastro.html', titulo_pagina="Página Inicial")

@app.route ('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confsenha = request.form['confsenha']

    if nome == '':
        return 'O campo nome é obrigatório'
    elif len(nome) < 3:
        return 'O nome deve ter pelo menos 3 caracteres'
    elif email =='':
        return 'O campo email é obrigatório'
    elif senha =='':
        return 'O campo nome é obrigatório'
    elif senha != confsenha:
        return 'As senhas não conferem'

    return f'Nome: {nome} <br> E-mail: {email} <br> Senha: {senha} <br> Confirmação: {confsenha}'

if __name__ == "__main__":
    app.run(debug=True)