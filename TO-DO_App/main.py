while True:
    user_decision = input("\nType 'Add' OR 'Show' OR 'Edit' OR 'Complete' OR 'Exit': ").strip().capitalize()

    # Read tasks and remove empty lines
    with open("todos.txt", "a"):
        pass

    with open("todos.txt", "r") as file:
        todos = [line.strip() for line in file if line.strip()]

    match user_decision:

        case "Add":
            todo = input("Enter a Task: ").strip()

            if todo:
                todos.append(todo.capitalize())

                with open("todos.txt", "w") as file:
                    for task in todos:
                        file.write(task + "\n")

                print("Task added successfully!")
            else:
                print("Task cannot be empty!")

        case "Show":
            if not todos:
                print("\nNo TODOs found.")
            else:
                print("\n------ YOUR TODO LIST ------")
                for index, task in enumerate(todos, start=1):
                    print(f"{index}. {task}")

        case "Edit":
            if not todos:
                print("No tasks to edit.")
                continue

            for index, task in enumerate(todos, start=1):
                print(f"{index}. {task}")

            try:
                num = int(input("Enter task number: ")) - 1

                if num < 0 or num >= len(todos):
                    print("Invalid task number.")
                    continue

                new_task = input("Enter new task: ").strip()

                if new_task:
                    todos[num] = new_task.capitalize()

                    with open("todos.txt", "w") as file:
                        for task in todos:
                            file.write(task + "\n")

                    print("Task updated successfully!")

            except ValueError:
                print("Please enter a valid number.")

        case "Complete":
            if not todos:
                print("No tasks to complete.")
                continue

            for index, task in enumerate(todos, start=1):
                print(f"{index}. {task}")

            try:
                num = int(input("Enter completed task number: ")) - 1

                if num < 0 or num >= len(todos):
                    print("Invalid task number.")
                    continue

                removed = todos.pop(num)

                with open("todos.txt", "w") as file:
                    for task in todos:
                        file.write(task + "\n")

                print(f"Completed: {removed}")

            except ValueError:
                print("Please enter a valid number.")

        case "Exit":
            print("Goodbye!")
            break

        case _:
            print("Invalid command.")