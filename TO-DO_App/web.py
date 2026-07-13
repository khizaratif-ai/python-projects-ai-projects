from flask import Flask, render_template, request, redirect
import functions

app = Flask(__name__)


@app.route("/")
def home():
    todos = functions.get_todos("todos.txt")
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    todos = functions.get_todos("todos.txt")

    new_todo = request.form["todo"]

    if new_todo:
        todos.append(new_todo + "\n")

    functions.write_todos("todos.txt", todos)

    return redirect("/")


@app.route("/complete/<todo>")
def complete(todo):

    todos = functions.get_todos("todos.txt")

    new_todos = []

    for item in todos:
        if item.strip() != todo.strip():
            new_todos.append(item)

    functions.write_todos("todos.txt", new_todos)

    return redirect("/")

@app.route("/edit/<todo>", methods=["GET", "POST"])
def edit(todo):

    todos = functions.get_todos("todos.txt")

    if request.method == "POST":

        new_todo = request.form["todo"]

        for index in range(len(todos)):

            if todos[index].strip() == todo.strip():

                todos[index] = new_todo + "\n"

                break

        functions.write_todos("todos.txt", todos)

        return redirect("/")


    return render_template(
        "edit.html",
        todo=todo
    )

@app.route("/exit")
def exit():

    return render_template("exit.html")


if __name__ == "__main__":
    app.run(debug=True)