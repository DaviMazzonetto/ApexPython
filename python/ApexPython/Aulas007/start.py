from flask import Flask, render_template
from pessoas import listar

app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/listar')
def listar_pessoas():
    lista = listar()
    return render_template('listar.html', pessoas = lista)

app.run(debug=True)


