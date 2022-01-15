from flask import Flask, render_template

application_name = "Tourism"
version = "1.0"

welcome_message = "Hey, Welcome to the journey!".format(application_name, version)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("indexx.html")

@app.route("/about")
def about():
    with open("About.html") as f:
        content = f.read()

    return content

@app.route("/Newsletter")
def Newsletter():
    with open("Newsletter.html") as f:
        content = f.read()

    return content

if __name__ == "__main__":
    print(welcome_message)
    app.run()





