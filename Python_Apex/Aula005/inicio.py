from flask import Flask, render_template, request, redirect 
from funcionarios import get_all, salvar_funcionario
#abrir na pagina web sobre pip, flask #sito o arquivo e digo oq quero importar do arquivo
#após instalar com o -pip install flsk no terminal
#comando abre o flask

app = Flask(__name__)
#comando padrão

@app.route('/') #pagina inicial
def inicio(): #uma funçao
    titulo = 'Olá, Sejam bem-vindos!'
    return render_template('index.html', mensagem=titulo)

@app.route('/funcionario') #pagina oficial/funcionario
def func(): #func significa funcionario
    funcionarios = get_all()
    return render_template('funcionario.html', funcionario = funcionarios)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form.get('nome')
    sobrenome = request.form.get('sobrenome')
    idade = request.form.get('idade')
    func1 = {
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade
    }    
    salvar_funcionario(func1)
    return redirect('/funcionario')

app.run(debug= True, host= '0.0.0.0')