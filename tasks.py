from conexao_orm import Base
from sqlalchemy import Column, Boolean, Integer, String, TIMESTAMP
from sqlalchemy.sql import func

class Task(Base):
    __tablename__ = 'tasks' #Define o nome da tabela
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column (String)
    creation_date = Column(TIMESTAMP, server_default=func.now()) #Insere automaticamente no BD a data em que o objeto foi criado
    done = Column(Boolean, default=False)
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
