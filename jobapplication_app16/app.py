from flask import Flask, render_template, request, url_for
from datetime import datetime
from email_utils import send_email

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    # Retrieve form data
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    start_date = request.form.get("start_date")
    occupation = request.form.get("occupation")
    qualification = request.form.get("qualification")
    experience = request.form.get("experience")
    skills = request.form.get("skills")
    cover_letter = request.form.get("cover_letter")

    # Format the selected date
    formatted_date = datetime.strptime(
        start_date,
        "%Y-%m-%d"
    ).strftime("%d %B %Y")

    # Create confirmation link
    confirmation_link = url_for(
        "confirmation",
        first_name=first_name,
        start_date=formatted_date,
        _external=True
    )

    # Send confirmation email
    send_email(
        receiver_email=email,
        first_name=first_name,
        start_date=formatted_date,
        confirmation_link=confirmation_link
    )

    return render_template(
        "success.html",
        first_name=first_name
    )


@app.route("/confirmation")
def confirmation():

    first_name = request.args.get("first_name")
    start_date = request.args.get("start_date")

    return render_template(
        "confirmation.html",
        first_name=first_name,
        start_date=start_date
    )


if __name__ == "__main__":
    app.run(debug=True)