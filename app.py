from main import show_options, add_task, list_tasks, complete_task, remove_task

while True:
    show_options()
    try:
        option = int(input("Selecione uma opção:\n"))
    except ValueError:
        print("Entrada deve ser um número!")
        continue

    match option:
        case 1:
            add_task()
        case 2:
            list_tasks()
        case 3:
            complete_task()
        case 4:
            remove_task()
        case 5:
            print("Saindo!")
            break
        case _:
            print("Opção inválida!")
            continue