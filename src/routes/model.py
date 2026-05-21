import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# 1. Carrega o arquivo .env (procure garantir que ele esteja na raiz do projeto)
load_dotenv()

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")

# Evita o erro do int('None') tratando a porta vazia
port_str = f":{db_port}" if db_port else ""
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}{port_str}/{db_name}"

# 2. Inicializa a engine e a classe base dos modelos
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# 3. Defina suas tabelas aqui (Exemplo: Tabela de Usuários)
class Usuario(Base):
    __tablename__ = 'usuarios'  # Nome da tabela no banco de dados

    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, primary_key=True)  # Email como chave primária
    senha = Column(String(255), nullable=False)
    bancos = relationship("Banco", back_populates="usuario")  # Relacionamento com a tabela de bancos

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Banco(Base):
    __tablename__ = 'bancos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    usuario_email = Column(String(100), ForeignKey('usuarios.email'), nullable=False)
    usuario = relationship("Usuario", back_populates="bancos")

    def __init__(self, nome, usuario_email):
        self.nome = nome
        self.usuario_email = usuario_email

# 4. Comando que efetivamente cria todas as tabelas no MySQL
if __name__ == "__main__":
    try:
        print("Conectando ao banco e criando tabelas...")
        # Lembre-se: O banco de dados já precisa existir no MySQL
        Base.metadata.create_all(engine)
        print("Tabelas criadas com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")