streamlit_app.py 
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>مرحباً بك في تطبيقي الأول على Render!</h1><p>تم النشر بنجاح.</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

