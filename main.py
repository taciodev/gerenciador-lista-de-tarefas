def add_task(task_list, task_name):
    task = {"name": task_name, "completed": False}
    task_list.append(task)


def view_tasks(task_list):
    print("\nLista de tarefas:")
    for index, task in enumerate(task_list, start=1):
        status = "✓" if task["completed"] else " "
        task_name = task['name']
        print(f"{index} - [{status}] {task_name}")


def update_task(task_list, task_index, new_task_name):
    adjusted_task_index = int(task_index) - 1
    if adjusted_task_index >= 0 and adjusted_task_index < len(tasks):
        task = task_list[adjusted_task_index]
        task["name"] = new_task_name
    else:
        print("\n⚠️ ÍNDICE DE TAREFA INVÁLIDO! ⚠️")


def complete_task(task_list, task_index):
    adjusted_task_index = int(task_index) - 1
    if adjusted_task_index >= 0 and adjusted_task_index < len(tasks):
        task = task_list[adjusted_task_index]
        task["completed"] = True
    else:
        print("\n⚠️ ÍNDICE DE TAREFA INVÁLIDO! ⚠️")


def delete_completed_tasks(task_list):
    for task in task_list:
        if task["completed"]:
            task_list.remove(task)


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
        task_name = input("Digite o nome da tarefa que deseja adicionar: ")
        add_task(tasks, task_name)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        view_tasks(tasks)
        print()
        task_index = input("Digite o número da tarefa que deseja atualizar: ")
        new_task_name = input(
            "Digite o novo nome da tarefa: ")
        update_task(tasks, task_index, new_task_name)
    elif choice == "4":
        view_tasks(tasks)
        print()
        task_index = input("Digite o número da tarefa que deseja completar: ")
        complete_task(tasks, task_index)
    elif choice == "5":
        delete_completed_tasks(tasks)
        view_tasks(tasks)
    elif choice == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


print("Programa finalizado com sucesso!")
