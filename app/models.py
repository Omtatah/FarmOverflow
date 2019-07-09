from . import db
from flask_login import UserMixin
from app import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

class Post(db.Model):
    __tablename__ = "posts"
    id  = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post = db.Column(db.String)
    time = db.Column(db.String)
    comments = db.relationship("Comment",backref = "post", lazy = "dynamic")
