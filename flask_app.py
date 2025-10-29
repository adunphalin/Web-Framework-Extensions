
from flask import Flask
from web_exts.flask_ext import FlaskExt

app = Flask(__name__)
ext = FlaskExt()
ext.init_app(app)

@app.route('/')
def index():
    return {'message': 'Hello from Flask with FlaskExt!'}

if __name__ == '__main__':
    app.run(debug=True)
