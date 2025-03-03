from flask import Flask
from models import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def drop_tables():
  db.drop_all()
  print("Tables dropped")

def create_tables():
  db.create_all()
  print("Tables created")

if __name__ == '__main__':
  with app.app_context():
    drop_tables()
    create_tables()
