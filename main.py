from conexao_orm import Base, engine, session
from tasks import Task
import csv
import json

#Cria as tabelas
Base.metadata.create_all(engine)

#Função para mostrar as opções
def show_options():
    print("Menu de opções:")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas pendentes")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover uma tarefa")
    print("5 - Exportar tarefas para arquivo")
    print("6 - Listar tarefas concluídas")
    print("7 - Sair")

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
      
#Função para listar todas as tarefas concluídas
def list_completed_tasks():
    tasks = session.query(Task).filter(Task.done == True).all()
    if not tasks:
        print("Nâo possui tarefas concluídas.")
        return
    print("Tarefas concluídas:")
    for task in tasks:
        print(f"{task.id} - {task.title}\n{task.description}")
       
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
    
#Função para exportar tarefas para arquivos JSON ou CSV
def export_tasks():
    tasks = session.query(Task).all()
    print("Deseja exportar em qual formato?")
    print("1 - CSV")
    print("2 - JSON")
    try:
        choice = int(input("> "))
    except ValueError:
        print("Entrada deve ser um número")
        return
    match choice:
        case 1:
            with open('tasks.csv', 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Título", "Descrição", "Concluída", "Data de Criação"]) #Escreve a primeira linha (colunas)
                for task in tasks: #Escreve todas as tarefas uma em cada linha
                    writer.writerow([task.id, task.title, task.description, task.done, task.creation_date])
                    print("Tarefas exportadas para tasks.csv!")
        case 2:
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump( #Método usado para escrever os dados no arquivo tasks.json
                    [
                        {
                            "id": task.id,
                            "title": task.title,
                            "description": task.description,
                            "done": task.done,
                            "creation_date": task.creation_date.isoformat() if task.creation_date else None,
                        }
                        for task in tasks
                    ],
                    file,
                    ensure_ascii=False, #Garante que caracteres especiais sejam exibidos corretamente
                    indent=4, #Adiciona indentação para tornar o JSON mais legível
                )
            print("Tarefas exportadas para tasks.json!")
        case _:
            print("Opção inválida.")