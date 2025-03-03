import os

class Config:
  SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:Hunter9039@localhost/gamble"
  # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SESSION_PERMANENT = False
  SESSION_TYPE = "filesystem"
  SECRET_KEY = "fewfwefewfewfwejfwehfkjewfw"