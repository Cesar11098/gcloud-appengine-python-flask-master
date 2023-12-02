from flask import Flask, render_template, request
from ply import lex

app = Flask(__name__)

tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION'
)

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f'Caracter erroneo: {t.value[0]}')
    t.lexer.skip(1)

analizadorLexico = lex.lex()

def analizarLexico(codigoFuente):
    analizadorLexico.input(codigoFuente)

    for token in analizadorLexico:
        print(token)

@app.route("/", methods=["GET", "POST"])
def homepage():
    cadenaProcesada = None
    if request.method == "POST":
        entrada = request.form.get("entrada")
        analizarLexico(entrada)
        cadenaProcesada = procesarCadena(entrada)

    return render_template("index.html", title="Automatosos", cadenaProcesada=cadenaProcesada)

@app.route("/semantico.html")
def analisisSemantico():
    return render_template("semantico.html")

@app.route("/sintactico.html")
def analisisSintactico():
    return render_template("sintactico.html")

@app.route("/lexico.html")
def analisisLexico():
    return render_template("lexico.html")

if __name__ == "__main__":
    app.run(debug=True)
