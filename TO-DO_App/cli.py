from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type 'Add', 'Show', 'Edit', 'Complete' or 'Exit' : ")
    user_action = user_action.capitalize()
    user_action = user_action.strip()

    if user_action.startswith('Add'):
        todo = user_action[4:]
        todo = todo.capitalize()

        todos = get_todos('todos.txt')

        todos.append(todo + "\n")

        write_todos('todos.txt', todos)
    elif user_action.startswith('Show'):
       #if not todos:
           #print("No todos are added!")
        #if todos:
         todos = get_todos('todos.txt')

         print("\n" + f"--------------YOUR TODO LIST HAVE {len(todos)} ITEMS--------------")
         for index, item in enumerate(todos, start = 1):
            item = item.strip('\n')
            row = f"{index}. {item}"
            print(row)
         print("\n")
    elif user_action.startswith('Edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos('todos.txt')
            new_todo = input("Enter new todo: ")
            new_todo = new_todo.capitalize()
            todos[number] = new_todo + "\n"
            write_todos('todos.txt', todos)
            print("\n""YOUR TODO LIST IS SUCCESSFULLY UPDATED!")
            print("\n" + f"--------------YOUR TODO LIST HAVE HAVE {len(todos)} ITEMS--------------")
            for index, item in enumerate(todos, start = 1):
                item = item.strip('\n')
                row = f"{index}. {item}"
                print(row)
            print("\n")
        except ValueError:
            print("\n" + "Enter the number of the task you want to edit!" + "\n")
            continue

    elif user_action.startswith('Complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos('todos.txt')
            todos.pop(number - 1)
            write_todos('todos.txt', todos)
            print("\n""YOUR TODO LIST IS SUCCESSFULLY UPDATED!")
            print("\n" + f"--------------YOUR TODO LIST HAVE {len(todos)} ITEMS--------------")
            for index, item in enumerate(todos, start = 1):
                item = item.strip('\n')
                row = f"{index}. {item}"
                print(row)
            print("\n")
        except ValueError:
            print("\n" + "Enter the number of the task you have completed!" + "\n")
            continue

    elif user_action.startswith('Exit'):
        print("\n" + "========================================GOODBYE!========================================")
        break
    else:
        print("Invalid Input")

