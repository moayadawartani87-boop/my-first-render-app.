from flask import Flask
app = Flask(__moayad__)

@app.route('/')
def hello_world():
    return 'Hello, World!'