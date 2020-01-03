from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1> Hello World <h1 />'


@app.route('/home')
def home():
    return '<h2> Welcome home fellow developers <h2 />'


if __name__ == "__main__":
    app.run(debug=True)
