from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "12345":
            message = "Kirish muvaffaqiyatli"
        else:
            message = "Login yoki parol xato"

    return render_template("index.html", message=message)

app.run(debug=True)
