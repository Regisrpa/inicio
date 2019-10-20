# Iporta biblioteca Flask
from flask import Flask, render_template, request, session, redirect

from views_principal.Pessoa import Pessoa
# Inicializa a aplicaçao instaciando Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '43r78934yt'

pessoas = []


@app.route("/listarPessoas")
def listarPessoas():
    print("teste blbllbbllbbl")
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


@app.route("/deletar")
def excluir():
    excl = None
    nome = request.args.get("nome")

    for pessoa in pessoas:
        if nome == pessoa.nome:
            excl = pessoa
            break
    if excl != None:
        pessoas.remove(excl)
    return listarPessoas()


@app.route("/produto")
def produto():
    return render_template("produto.html")


@app.route("/vendedor")
def vendedor():
    return render_template("vendedor.html")


@app.route("/login")
def login():
    login = request.args.get("login")
    senha = request.args.get("senha")
    if login == "regis" and senha == "teste123":
        session['usuario'] = login
        return redirect("/index")
    else:
        # informa que o login é inválido
        return render_template("exibir_mensagem", mensagem="Login/senha inválido(s)")


@app.route("/form_login")
def form_login():
    return render_template("form_login.html")


@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/index")


# executa a aplicaçao
app.run()
