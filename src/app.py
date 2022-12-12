from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'super secret key'

# Conexão ao banco de dados

def LoadConfig():
    config = {}
    conf = open("config.conf", "r")
    for line in conf:
        line = line.strip()
        if line[:4] == 'host':
            config['host'] = line[7:]
        elif line[:4] == 'port':
            config['port'] = int(line[6:])
        elif line[:4] == 'user':
            config['user'] = line[7:]
        elif line[:8] == 'password':
            config['password'] = line[11:]
        elif line[:2] == 'db':
            config['db'] = line[5:]
    conf.close()
    return config

config = LoadConfig()

app.config['MYSQL_HOST'] = config['host']
app.config['MYSQL_PORT'] = config['port'] #Caso a porta seja a padrão, comentar linha.
app.config['MYSQL_USER'] = config['user']
app.config['MYSQL_PASSWORD'] = config['password']
app.config['MYSQL_DB'] = config['db']

mysql = MySQL(app)

#Rotas

@app.route("/")
@app.route("/Home.html")
def index():
    return render_template('Home.html')


@app.route("/Contato.html", methods = ['POST','GET'])
def contato():
    if request.method == "POST": 

        cursor = mysql.connection.cursor()

        txt_email = request.form['email']
        txt_assunto = request.form['assunto']
        txt_descricao = request.form['descricao']

        txtSQL = f' INSERT INTO tb_contato (email, assunto, descricao) VALUES ("{txt_email}", "{txt_assunto}", "{txt_descricao}")' 

        cursor.execute(txtSQL)
        mysql.connection.commit()  
        cursor.close() 
        
    return render_template('Contato.html')


@app.route("/Quem Somos.html")
def quemsomos():
    return render_template('Quem Somos.html')


if __name__ == "__main__":
    app.run(debug=True)
