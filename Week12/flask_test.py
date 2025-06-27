from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<h1>Hello, Flask!</h1>"

@app.route("/bye")
def bye():
    return "<h1>Goodbye, Flask!</h1>"

@app.route("/username/<name>")
def learn(name):
    return f"<h1>{name} is learning Flask!</h1>"

if __name__ == "__main__":
    app.run(debug=True)