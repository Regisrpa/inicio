# Iporta biblioteca Flask
from flask import Flask, render_template, request

# Inicializa a aplicaçao instaciando Flask
from Pessoa import Pessoa

app = Flask(__name__)

pessoas = []


@app.route("/listarPessoas")
def listarPessoas():
    return render_template("listarPessoas.html", listar=pessoas)


# Atribuiçao da rota web
@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/cadastrarPessoa")
def cadastrarPessoa():
    return render_template("cadastrarPessoa.html")


@app.route("/incluirPessoa")
def incluir():
    # obter os parâmetros do formulário
    nome = request.args.get("nome")
    endereco = request.args.get("endereco")
    telefone = request.args.get("telefone")
    email = request.args.get("email")
    # montar uma mensagem de resposta
    nova = Pessoa(nome, endereco, telefone, email)
    pessoas.append(nova)

    return render_template("mensagem.html", mensagem="Pessoa inserida com sucesso!")

app.route("/excluir")
def excluir():
    excluir=None
    nome=request.args.get("nome")
    for pessoa in pessoas:
        if nome == pessoa.nome:
            excluir=pessoa
            break
        if excluir != None:
            pessoas.remove(excluir)
        return listarPessoas()


@app.route("/produto")
def produto():
    return render_template("produto.html")


@app.route("/vendedor")
def vendedor():
    return render_template("vendedor.html")


# executa a aplicaçao
app.run()
