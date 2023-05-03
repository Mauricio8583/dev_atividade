from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///atividades.db")
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoa(Base):
    __tablename__ = "pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return "<Pessoa {}>".format(self.nome)

class Atividades(Base):
    __tablename__ = "atividades"
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey("pessoa.id"))
    pessoa = relationship("Pessoa")

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()