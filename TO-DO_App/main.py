while True:
    user_action = input("Type 'Add', 'Show', 'Edit', 'Complete' or 'Exit' : ")
    user_action = user_action.capitalize()
    user_action = user_action.strip()

    match user_action:
        case 'Add':
            todo = input("Enter a todo: ") + "\n"
            todo = todo.capitalize()

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'Show':
#            if not todos:
#               print("No todos are added!")
#            if todos:
             print("\n" + f"--------------YOUR TODO LIST--------------")
             for index, item in enumerate(todos, start = 1):
                row = f"{index}. {item}"
                print(row)
             print("\n")
        case 'Edit':
            number = int(input("Enter the number of the todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo
            print("\n""YOUR TODO LIST IS SUCCESSFULLY UPDATED!")
            print("\n" + f"--------------YOUR TODO LIST HAVE--------------")
            for index, item in enumerate(todos, start = 1):
                row = f"{index}. {item}"
                print(row)
            print("\n")

        case 'Complete':
            number = int(input("Enter the number of the todo to complete: "))
            number = number - 1
            todos.pop(number)
            print("\n""YOUR TODO LIST IS SUCCESSFULLY UPDATED!")
            print("\n" + f"--------------YOUR TODO LIST HAVE {len(todos)} ITEMS--------------")
            for index, item in enumerate(todos, start = 1):
                row = f"{index}. {item}"
                print(row)
            print("\n")

        case 'Exit':
            print("\n" + "========================================GOODBYE!========================================")
            break
        case _:
            print("Invalid input")

