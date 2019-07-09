from . import auth
from flask import redirect,render_template,url_for
from flask_login import login_user,logout_user
from .forms import RegistrationForm,LoginForm
from ..models import User
from ..email import create_mail
