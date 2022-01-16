from flask import Flask, request, render_template
import pickle

application_name = "Tourism"
version = "1.0"

welcome_message = "Hey, Welcome to the journey!".format(application_name, version)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("login.html")
database={'sana':'123'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('indexx.html',name=name1)

@app.route("/")
def index():
    return render_template("indexx.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/Register")
def Register():
    return render_template("Register.html")

@app.route("/Locate")
def Locate():
    return render_template("Locate.html")

@app.route("/Newsletter")
def Newsletter():
    return render_template("Newsletter.html")

@app.route("/Feedback")
def Feedback():
    return render_template("Feedback.html")




if __name__ == "__main__":
    print(welcome_message)
    app.run()





