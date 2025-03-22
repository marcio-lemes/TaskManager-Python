# **Sistema de Gerenciamento de Tarefas (To-Do List)**   

---

## **Descrição**  
Este projeto é um sistema de gerenciamento de tarefas (To-Do List) que utiliza **SQLAlchemy** como ORM (Object-Relational Mapping) para interagir com um banco de dados **PostgreSQL**. Ele permite a criação, listagem, conclusão, remoção e exportação de tarefas, oferecendo uma interface simples e eficiente para o gerenciamento de atividades diárias.

---

## **Funcionalidades**  
- **Adicionar Tarefas**: Cria novas tarefas com título e descrição.  
- **Listar Tarefas Pendentes**: Exibe todas as tarefas que ainda não foram concluídas.  
- **Listar Tarefas Concluídas**: Exibe todas as tarefas que foram marcadas como concluídas.  
- **Marcar Tarefa como Concluída**: Altera o status de uma tarefa para "concluída".  
- **Remover Tarefas**: Remove uma tarefa do banco de dados.  
- **Exportar Tarefas**: Exporta todas as tarefas para arquivos **CSV** ou **JSON**.  
- **Validação de Entradas**: Garante que os dados inseridos pelo usuário sejam válidos.  

---

## **Tecnologias e Habilidades Usadas**
- Linguagem Python;
- Operações CRUD;
- ETL (Extract, Transfrom, Load);
- Modelagem de Banco de Dados;
- Uso de ORM (SQLAlchemy);
- Manipulação de Arquivos (JSON e CSV);
- Validação de Dados;
- Tratamento de Exceções;
- Desenvolvimento de CLI

---

## **Requisitos**  
Para executar este projeto, você precisará ter instalado:  
- Python 3.x  
- Biblioteca `SQLAlchemy` (`pip install sqlalchemy`)
- Biblioteca `psycopg2` (`pip install psycopg2`)
- PostgreSQL rodando localmente.  

---

## **Como Usar**  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/to-do-list.git

2. Instale as dependências:  
   ```bash
   pip install sqlalchemy psycopg2

3. Configure o banco de dados PostgreSQL:
- Crie um banco de dados chamado to_do.
- Atualize as credenciais no arquivo conexao_orm.py (usuário, senha, host).

4. Execute o script principal:
    ```bash
    python app.py

---

## **Estrutura do Projeto**
### **Arquivos Principais**
Arquivos Principais
- conexao_orm.py: Configura a conexão com o banco de dados e define a base para os modelos.
- tasks.py: Define a classe Task, que representa a tabela de tarefas.
- main.py: Contém a lógica do sistema, incluindo funções para adicionar, listar, concluir, remover e exportar tarefas.
- app.py: Script principal que inicia a aplicação e exibe o menu interativo.

---

## **Contato**
- Márcio Simões Lemes
- GitHub: marcio-lemes
- Email: devmarciolemes@gmail.com