from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

db = SQLAlchemy()
bcrypt = Bcrypt()

class Users(db.Model, UserMixin):
  __tablename__ = "users"
  id = db.Column(db.Integer(), primary_key=True)
  username = db.Column(db.String(50), nullable=False)
  phone_number = db.Column(db.String(10), nullable=False)
  last_login = db.Column(db.DateTime())
  wallet = db.Column(db.Integer, default=0)
  referral_code = db.Column(db.String(10), nullable=False)
  session = db.relationship("Session", backref="owner", lazy=True)
  payment = db.relationship("Payment", backref="payment", lazy=True)

class Session(db.Model):
  __tablename__ = "session"
  id = db.Column(db.Integer(), primary_key=True)
  unique_id = db.Column(db.Integer(), unique=True)
  date_started = db.Column(db.DateTime(), nullable=False)
  user = db.Column(db.Integer(), db.ForeignKey("users.id"))
  is_active = db.Column(db.Boolean(), default=True)
  rounds = db.relationship("Rounds", backref="round", lazy=True)

class Rounds(db.Model):
  __tablename__ = "rounds"
  id = db.Column(db.Integer(), primary_key=True)
  unique_id = db.Column(db.Integer(), unique=True)
  date_started = db.Column(db.DateTime())
  score = db.Column(db.Integer, default=0)
  session = db.Column(db.Integer(), db.ForeignKey("session.id"))
  is_active = db.Column(db.Boolean(), default=True)

class Payment(db.Model):
  __tablename__ = "payment"
  id = db.Column(db.Integer(), primary_key=True)
  unique_id = db.Column(db.Integer(), unique=True)
  MerchantRequestID = db.Column(db.String(50))
  CheckoutRequestID = db.Column(db.String(50))
  MpesaReceiptNumber = db.Column(db.String(50))
  transactionDate = db.Column(db.DateTime())
  amount = db.Column(db.Integer())
  phone_number = db.Column(db.String(10))
  is_pending = db.Column(db.Boolean(), default=True)
  is_confirmed = db.Column(db.Boolean(), default=False)
  is_failed = db.Column(db.Boolean(), default=False)
  user = db.Column(db.Integer(), db.ForeignKey("users.id"))
