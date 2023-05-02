from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Silv@2311'
app.config['MYSQL_DB'] = 'DevWeb'

mysql = MySQL(app)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/quemSomos")
def quemSomos():
    return render_template("quemSomos.html")


@app.route("/contato", methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)",(email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return 'sucesso'
    return render_template('contato.html')

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

    return render_template('user.html', userDetails=userDetails)