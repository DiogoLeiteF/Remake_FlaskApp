from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # criamos o servidor web flask
app.config['DEBUG'] = True  # o debug=True faz com que o servidor se reinicie sozinho sempre que modificamos o
# codigo ou reiniciamos o servidor
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tarefas.db'  # linha para criar a ligação da app à db/
# a ligação e efetuada depois de criado o diretorio e a db
db = SQLAlchemy(app)  # Cursor para a base de dados SQLite


# no terminal criamos a base de dados no diretorio criado "database" -->sqlite3 database/tarefas.db
# podemos confirmar as db existentes com o comando -->.databases   #devolve a localização exata da bd
# o comando -->.tables  #devolve as tabelas existentes

class Tarefa(db.Model):
    # criar a tabela 'tarefas' com 3 colunas de dados: 1-id unico; 2- tarefa; 3- estado da tarefa
    __tablename__ = 'tarefas'
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(200))
    feita = db.Column(db.Boolean)


db.create_all()  # Criação de tabelas
db.session.commit()  # Execução de tarefas pendentes


# correr novamente a app.py a tabela será criada
# verificar com os comandos:
# -->sqlite3 tarefas.db
# -->.databases
# -->.tarefas
# select name from pragma_table_info('tarefas');  # efectuar uma consulta

# criar o objeto tarefa com os dados do form e atualizar a tabela terefas
@app.route('/criar-tarefa', methods=['POST'])
def criar():
    tarefa = Tarefa(conteudo=request.form['conteudo_tarefa'], feita=False)
    db.session.add(tarefa)
    db.session.commit()
    return 'tarefa guardada'


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


# todo 13 pag 55