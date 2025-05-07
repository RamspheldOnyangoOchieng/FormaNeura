from app import create_app
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
from app import db
from app import routes, models, forms
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
