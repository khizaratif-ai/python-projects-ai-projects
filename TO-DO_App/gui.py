import functions
import FreeSimpleGUI as sg

label = sg.Text("Type Your To-do Here!")
input_box = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")

window = sg.Window('My To-do App', layout=[[label], [input_box, add_button]])
window.read()
print("Todo noted succesfully")
window.close()