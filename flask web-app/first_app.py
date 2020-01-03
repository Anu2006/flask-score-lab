from flask import Flask  # importing Flask class from flask

app = Flask(__name__)  # name is a variable that stores the module name. we pass it to the Flask class
# as an argument to create our flask server. other things it will configure it self.


@app.route('/')  # app.route is a decorater that tells the function page it lands. here this function will run on main page
def hello_world():
    return '<h1> Hello World <h1 />'


@app.route('/home')
def home():
    return '<h2> Welcome home fellow developers <h2 />'


if __name__ == "__main__":  # if this script is not imported from another module
    app.run(debug=True)  # run the app with debug mode on
