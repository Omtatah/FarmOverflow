from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager




class  User(UserMixin,db.Model):
    __tablename__ ='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255),unique=True,index=True)
    password_hash=db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    about = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    comment = db.relationship('Comments',backref='user', lazy='dynamic')
    commentscom = db.relationship('CommentsCom', backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You can`t see this')
    @password.setter
    def password(self,password):
