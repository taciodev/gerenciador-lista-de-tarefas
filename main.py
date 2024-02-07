def add_task(task_list, task_name):
    task = {"name": task_name, "completed": False}
    task_list.append(task)


def view_tasks(task_list):
    ...


def update_task(task_list):
    ...


def complete_task(task_list):
    ...


def delete_completed_tasks(task_list):
    ...


tasks = []

while True:
    print("\n*********************************************")
    print("*          Menu de Lista de Tarefas         *")
    print("*-------------------------------------------*")
    print("* 1. Adicionar tarefa                      *")
    print("* 2. Ver tarefas                           *")
    print("* 3. Atualizar tarefa                      *")
    print("* 4. Completar tarefa                      *")
    print("* 5. Deletar tarefas completadas           *")
    print("* 6. Sair                                  *")
    print("*********************************************")

    choice = input("\nQual a sua escolha: ")

    if choice == "1":
        task_name = input("Digite o nome da tarefa que deseja adcionar: ")
        add_task(tasks, task_name)
    elif choice == "2":
        ...
    elif choice == "3":
        ...
    elif choice == "4":
        ...
    elif choice == "5":
        ...
    elif choice == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


print("Programa finalizado com sucesso!")
