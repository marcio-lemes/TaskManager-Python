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
    title = input("Informe o nome da tarefa:\n") #Pede para o usuário digitar o nome da tarefa
    if not title: #Valida se o título não vazio
        print("O nome da tarefa não pode ficar em branco.")
        return
    description = input("Se quiser, informe a descrição da tarefa:\n") #Pede para o usuário digitar a descrição da tarefa
    task = Task(title, description) #Cria o objeto da classe com os atributos que o usuário passar
    try:
        session.add(task) #Adiciona no banco de dados
        session.commit() #Realiza a mudança
        print ("Tarefa adicionada com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar tarefa: {e}")
    
#Função para listar todas as tarefas pendentes
def list_tasks():
    tasks = session.query(Task).filter(Task.done == False) #Atribui à uma lista os resultados da pesquisa: Pesquisa no banco de dados (query), objetos da classe Task (no caso objetos da tabela tasks), e filtra os resultados que tem o atributo done = False, assim trazendo as tarefas que ainda não foram concluídas
    if not tasks: #Valida se a lista está vazia
        print("Nenhuma tarefa pendente.")
        return
    print("Tarefas pendentes:")
    for task in tasks: #Percorre a lista de resultados (tasks) que veio do banco de dados
        print(f"{task.id} - {task.title}\n{task.description}")
      
#Função para listar todas as tarefas concluídas
def list_completed_tasks():
    tasks = session.query(Task).filter(Task.done == True).all() #Também atribui à lista os resultados de uma pesquisa no banco de dados, nesse caso, ele vai buscar na tabela tasks todos os resultados que tiverem o atributo done = True, assim trazendo as tarefas que foram concluídas
    if not tasks: #Valida se a lista está vazia
        print("Nâo possui tarefas concluídas.")
        return
    print("Tarefas concluídas:")
    for task in tasks: #Percorre a lista de resultados (tasks) que veio do banco de dados
        print(f"{task.id} - {task.title}\n{task.description}")
       
#Função para concluir tarefas
def complete_task():
    try:
        task_id = int(input("Digite o ID da tarefa que deseja concluir:\n")) #Pede para o usuário o ID da tarefa que deseja marcar
    except ValueError: #Em caso do usuário digitar algo que não seja um número, retorna a mensagem de erro.
        print("Entrada deve ser um número!")
        return
    task = session.query(Task).filter(Task.id == task_id).first() #Pesquisa na tabela tasks do banco de dados, comparando/filtrando o resultado pelo atributo ID, depois atribui o resultado à variável
    if not task: #Valida se a tarefa foi encontrada
        print(f"Tarefa de ID {task_id} não encontrada.")
        return
    task.done = True #Altera o atributo done para True, assim "concluindo a tarefa"
    session.commit() #Realiza a mudança no banco de dados
    print(f"Tarefa '{task.title}' marcada com sucesso!")
    
#Função para remover tarefas
def remove_task():
    try:
        task_id = int(input("Digite o ID da tarefa que deseja remover:\n")) #Pede para o usuário o ID da tarefa que deseja remover
    except ValueError: #Em caso do usuário digitar algo que não seja um número, retorna a mensagem de erro.
        print("Entrada deve ser um número!")
        return
    task = session.query(Task).filter(Task.id == task_id).first() #Pesquisa na tabela tasks do banco de dados, comparando/filtrando o resultado pelo atributo ID, depois atribui o resultado à variável
    if not task: #Valida se a tarefa foi encontrada
        print(f"Tarefa de ID {task_id} não encontrada.")
        return
    session.delete(task) #Ação para deletar a tarefa
    session.commit() #Realiza a mudança no banco de dados
    print(f"Tarefa ID {task_id} removida com sucesso!")
    
#Função para exportar tarefas para arquivos JSON ou CSV
def export_tasks():
    tasks = session.query(Task).all() #Pesquisa todos os resultados da classe Task (tabela tasks no banco de dados)
    print("Deseja exportar em qual formato?")
    print("1 - CSV")
    print("2 - JSON")
    try:
        choice = int(input("> ")) #Pede para o usuário escolher qual opção que ele deseja exportar o arquivo
    except ValueError: #Em caso do usuário digitar algo que não seja um número, retorna a mensagem de erro.
        print("Entrada deve ser um número")
        return
    match choice:
        case 1:
            with open('tasks.csv', 'w', encoding='utf-8') as file: #Abre/Cria o arquivo
                writer = csv.writer(file) #Cria um objeto da biblioteca csv que é responsável por escrever dados em um arquivo no formato CSV
                writer.writerow(["ID", "Título", "Descrição", "Concluída", "Data de Criação"]) #Escreve a primeira linha (colunas)
                for task in tasks: #Itera sobre a lista de tarefas
                    writer.writerow([task.id, task.title, task.description, task.done, task.creation_date]) #Escreve todos os atributos da tarefa na linha
                    print("Tarefas exportadas para tasks.csv!")
        case 2:
            with open('tasks.json', 'w', encoding='utf-8') as file: #Abre/Cria o arquivo
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