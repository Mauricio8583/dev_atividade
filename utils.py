from models import Pessoa
from models import db_session

def inserir_pessoa():
    pessoa = Pessoa(nome="Jonh Doe", idade=33)
    db_session.add(pessoa)
    db_session.commit()
    

def consulta_pessoas():
    pessoa = Pessoa.query.all()
    print(pessoa)    


def alterar_pessoa():
    pessoa = Pessoa.query.filter_by(nome="Jonh Doe").first()
    pessoa.idade = 28
    db_session.add(pessoa)
    db_session.commit()

def excluir_pessoa():
    pessoa = Pessoa.query.filter_by(nome="Jonh Doe").first()
    db_session.delete(pessoa)
    db_session.commit()

if __name__ == "__main__":
    consulta_pessoas()