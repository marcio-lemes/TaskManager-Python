from sqlalchemy import create_engine #Função que instancia um objeto Engine que é responsável por gerenciar a conexão com o BD
from sqlalchemy.orm import sessionmaker #Função que cria uma classe de sessão, usada para integragir com o banco de dados de forma transacional
from sqlalchemy.ext.declarative import declarative_base #Função que cria uma classe base para definição de modelo de dados (tabelas)

user = 'postgres'
password = '1234'
host = 'localhost'
database = 'to_do'

try:
    DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}' #URI que será usada para se conectar ao banco de dados
    engine = create_engine(DATABASE_URI) #Criando a Engine (principal interface para a comunicação com o banco de dados e gerencia a conexão) com a URI
    Session = sessionmaker(bind=engine) #Criando a classe de sessão vinculada ao Engine
    session = Session() #Instância da Sessão, essa instância será utilizada para realizar operações CRUD no banco de dados
    Base = declarative_base() #Classe base que será usada para definir os modelos de dados de forma declarativa, assim, permitindo definir tabelas como classes Python.
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    