todos = []

while True:
    user_decision = input("Type 'Add' OR 'Show' OR 'Exit: ")
    user_decision = user_decision.capitalize()
    user_decision = user_decision.strip()


    match user_decision:
        case 'Add':
            todo = input("Enter a Task: ")
            todos.append(todo.capitalize())
#bitwise thing "|"
        case 'Show' | 'Display':
             for item in todos:
                 item = item.title()
                 print(item)
        case 'Exit':
             print("Goodbye :)")
             break
#case of any random entered string such as
#"asdjhgs" rather thn "ADD/EXIT/SHOW/DISPLAY"
        case _:
             print('Hi There! You Entered an unknown command')



