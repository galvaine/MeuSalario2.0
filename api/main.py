from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bikbUqMiojthxfj5@abundantly-flying-snook.data-1.use1.tembo.io:5432/postgres'
db = SQLAlchemy(app)

#Criando o modelo das tabelas do banco de dados
class Cadastro(db.Model):
    __tablename__ = 'my_table'
    nome = db.Column("Nome", db.String(150))
    telefone = db.Column("Telefone", db.BigInteger)
    cpf = db.Column("Cpf", db.BigInteger, primary_key = True)
    endereço = db.Column("Endereço", db.String(250))

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    return render_template ('cadastro.html')

#Leitura do banco de dados
@app.route('/visualizar', methods=["GET"])
def visualizar():
    cadastro = Cadastro.query.all()
    return render_template('visualizar.html', cadastro=cadastro)

@app.route('/editar', methods=["POST", "GET"])
def editar():
    Editar_cadastro = Cadastro.query.all()
    return render_template('editar.html',Editar_casdastro=Editar_cadastro)

@app.route('/cadastrar', methods=["POST"])
def cadastrar():
    nome = request.form['nome'].capitalize().strip()
    telefone = request.form['telefone'].strip()
    cpf = request.form['cpf'].strip()
    endereço = request.form['endereço'].capitalize().strip()
    formatado_telefone = int(telefone)
    formatado_cpf = int(cpf)

    #Validação se ja existe um mesmo cpf cadastrado
    Existe_cpf = Cadastro.query.filter_by(cpf=formatado_cpf).first()
    if Existe_cpf:
        return "Erro: Cpf ja cadastrado!"
    
    existe_nome = Cadastro.query.filter_by(nome=nome).first()
    if existe_nome:
        return "Erro: Nome ja existe no banco!"

    novo_usuario = Cadastro(nome = nome, telefone=formatado_telefone,cpf=formatado_cpf,endereço=endereço)
    db.session.add(novo_usuario)
    db.session.commit()
    return redirect('/cadastro')

@app.route('/deletar/<int:cpf_usuario>', methods=["POST"])
def deletar(cpf_usuario):
    usuario = Cadastro.query.get(cpf_usuario)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
    return redirect('/editar')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)