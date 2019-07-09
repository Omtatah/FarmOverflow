from . import main
from flask_login import current_user, login_required
from .forms import AddPostForm,SubscribeForm,AddComment,EditBio
from ..models import Post,User,Comment,Subscriber
from ..requests import get_quotes
from flask import redirect,url_for,render_template,flash,request
from .. import db,photos
from datetime import datetime
from app.email import create_mail
