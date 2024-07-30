from flask import Flask,render_template

app = Flask(__name__)

#criar a 1º pagina
@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/contatos')
def contatos():
    return render_template("contatos.html")

#colocar site no ar
if __name__ =="__main__":
    app.run(debug =True)
