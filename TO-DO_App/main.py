while True:
    user_action = input("Type 'Add', 'Show', 'Edit', 'Complete' or 'Exit' : ")
    user_action = user_action.capitalize()
    user_action = user_action.strip()

    if 'Add' in user_action:
        todo = user_action[4:]
        todo = todo.capitalize()

        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()

        todos.append(todo)

        file = open('todos.txt', 'w')
        file.writelines(todos)
        file.close()
    elif 'Show' in user_action:
       #if not todos:
           #print("No todos are added!")
        #if todos:
         file = open('todos.txt', 'r')
         todos = file.readlines()
         file.close()

         print("\n" + f"--------------YOUR TODO LIST HAVE {len(todos)} ITEMS--------------")
         for index, item in enumerate(todos, start = 1):
            item = item.strip('\n')
            row = f"{index}. {item}"
            print(row)
         print("\n")
    elif 'Edit' in user_action:
        number = int(user_action[5:])
        number = number - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        print("\n""YOUR TODO LIST IS SUCCESSFULLY UPDATED!")
        print("\n" + f"--------------YOUR TODO LIST HAVE--------------")
        for index, item in enumerate(todos, start = 1):
            item = item.strip('\n')
            row = f"{index}. {item}"
            print(row)
        print("\n")

    elif 'Complete' in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todos.pop(number - 1)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        print("\n""YOUR TODO LIST IS SUCCESSFULLY UPDATED!")
        print("\n" + f"--------------YOUR TODO LIST HAVE {len(todos)} ITEMS--------------")
        for index, item in enumerate(todos, start = 1):
            item = item.strip('\n')
            row = f"{index}. {item}"
            print(row)
        print("\n")

    elif 'Exit' in user_action:
        print("\n" + "========================================GOODBYE!========================================")
        break
    else:
        print("Invalid Input")

