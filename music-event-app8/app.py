from flask import Flask, render_template, request
from event_api import search_events

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():

    keyword = request.form.get("keyword")

    if keyword == "":
        return render_template(
            "results.html",
            keyword="",
            events=[],
            message="Please enter an artist or event name."
        )

    events = search_events(keyword)

    if len(events) == 0:
        message = "No music events found."
    else:
        message = ""

    return render_template(
        "results.html",
        keyword=keyword,
        events=events,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)