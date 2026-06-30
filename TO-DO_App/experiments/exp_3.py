todos = []

while True:
    user_decision = input("Type 'Add' OR 'Show' OR 'Edit' OR 'Complete' OR 'Exit': ")
    user_decision = user_decision.capitalize()
    user_decision = user_decision.strip()


    match user_decision:
        case 'Add':
            todo = input("Enter a Task: ")
            todos.append(todo.capitalize())
        case 'Show':
            if not todos:
                print('  ')
                print("============================")
                print("NO TODO FOUND, ADD NEW TODOS")
                print("============================")
                print('  ')
            for index, task in enumerate(todos, start=1):
                fnf_task = f"{index}. {task}"
                print(fnf_task)
        case 'Edit':
            for index, task in enumerate(todos, start=1):
                fnf_task = f"{index}. {task}"
                print(fnf_task)
            existing_todo_num = int(input('Enter the number of the Todo you want to edit/replace: '))
            existing_todo_num = existing_todo_num - 1
            new_todo = input("Enter a new Task: ")
            todos[existing_todo_num] = new_todo.capitalize()
            for index, task in enumerate(todos, start=1):
                fnf_task = f"{index}. {task}"
                print(fnf_task)
            print('  ')
            print("=================================")
            print("Your List Is Successfully Edited!")
            print("=================================")
            print('  ')
        case 'Complete':
            for index, task in enumerate(todos, start=1):
                fnf_task = f"{index}. {task}"
                print(fnf_task)
            index = int(input("Enter the number of task that's complete: "))
            index = index - 1
            todos.pop(index)
            for index, task in enumerate(todos, start=1):
                fnf_task = f"{index}. {task}"
                print(fnf_task)
            if not todos:
                print('  ')
                print("==================================")
                print("ALL TASKS COMPLETED SUCCESSFULLY!")
                print("==================================")
                print('  ')
        case 'Exit':
             print('  ')
             print("==============={-Goodbye-}===============")
             break
        case _:
            print('  ')
            print("==================================")
            print("NO SUCH COMMAND FOUND!")
            print("==================================")




