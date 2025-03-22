from conexao_orm import Base, engine, session
from tasks import Task

#Cria as tabelas
Base.metadata.create_all(engine)

#Função para mostrar as opções
def show_options():
    print("Menu de opções:")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas pendentes")
    print("3 - Marcar tarefa como concluída")
    print("4 - Sair")

#Função para adicionar uma tarefa
def add_task():
    title = input("Informe o nome da tarefa:\n")
    if not title:
        print("O nome da tarefa não pode ficar em branco.")
        return
    description = input("Se quiser, informe a descrição da tarefa:\n")
    task = Task(title, description) #Cria o objeto da classe com os atributos que o usuário passar
    try:
        session.add(task) #Adiciona no banco de dados
        session.commit() #Realiza a mudança
        print ("Tarefa adicionada com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar tarefa: {e}")
    
#Função para listar todas as tarefas pendentes
def list_tasks():
    tasks = session.query(Task).filter(Task.done == False)
    if not tasks:
        print("Nenhuma tarefa pendente.")
        return
    print("Tarefas pendentes:")
    for task in tasks:
        print(f"{task.id} - {task.title}")
        
#Função para concluir tarefas
def complete_task():
    try:
        task_id = int(input("Digite o ID da tarefa que deseja concluir:\n"))
    except ValueError:
        print("Entrada deve ser um número!")
        return
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        print(f"Tarefa de ID {task_id} não encontrada.")
        return
    task.done = True
    session.commit()
    print(f"Tarefa '{task.title}' marcada com sucesso!")
    
#Função para remover tarefas
def remove_task():
    try:
        task_id = int(input("Digite o ID da tarefa que deseja remover:\n"))
    except ValueError:
        print("Entrada deve ser um número!")
        return
    task = session.query(Task).filter(Task.id == task_id).first()
    if not task:
        print(f"Tarefa de ID {task_id} não encontrada.")
        return
    session.delete(task)
    session.commit()
    print(f"Tarefa ID {task_id} removida com sucesso!")