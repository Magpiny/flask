from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Magpiny Blog<h1> <br> <p>Welcome to my page and thanks for visiting...</p>'

@app.route('/user/<name>')
def user(name):
    return '<h3>Hello {}</h3>'.format(name)

