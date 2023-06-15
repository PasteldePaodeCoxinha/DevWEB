from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config["MYSQL_HOST"] = "db"
app.config["MYSQL_USER"] = "unes"
app.config["MYSQL_PASSWORD"] = "1234"
app.config["MYSQL_DB"] = "devweb"

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/quemSomos")
def quemSomos():
    return render_template("quemSomos.html")


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        email = request.form["email"]
        assunto = request.form["assunto"]
        descricao = request.form["descricao"]

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)",
            (email, assunto, descricao),
        )

        mysql.connection.commit()

        cur.close()

        return "<h1>sucesso: <a href='./contato'>VOLTAR</a></h1>"
    return render_template("contato.html")


@app.route("/user")
def user():
    cur = mysql.connection.cursor()

    user = cur.execute("Select * From contatos")
    mysql.connection.commit()

    if user > 0:
        userDetails = cur.fetchall()
    else:
        userDetails = "Não tem nada"
    cur.close()

    return render_template("user.html", userDetails=userDetails)
