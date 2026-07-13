import functions
import FreeSimpleGUI as sg

label = sg.Text("Type Your To-do Here!")
input_box = sg.InputText(tooltip="Enter Todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values= functions.get_todos('todos.txt'), key='todos',
                      size =(45, 10), enable_events=True, )
edit_button = sg.Button("Edit")

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos('todos.txt')
            new_todo = values['todo'] + "\n"

            todos.append(new_todo)
            functions.write_todos('todos.txt', todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_be_edited = values['todos'][0]
            new_todo = values['todos']

            todos = functions.get_todos('todos.txt')
            index = todos.index(todo_to_be_edited)
            todos[index] = new_todo
            functions.write_todos('todos.txt', todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()