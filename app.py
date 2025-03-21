from main import show_options, add_task, list_tasks, complete_task

while True:
    show_options()
    option = int(input("Selecione uma opção:\n"))

    match option:
        case 1:
            add_task()
        case 2:
            list_tasks()
        case 3:
            complete_task()
        case 4:
            print("Saindo!")
            break
        case _:
            print("Opção inválida!")
            continue