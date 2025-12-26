# my-first-render-app
Topics: flask, python, web-app, starter-template, render
from flask import Flask
import os

app = Flask__name__

@app.route('/')
def home():
    return "<h1>My First App on Render! 🚀</h1><p>Done by [اسمحك هنا]</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
flask
gunicorn
