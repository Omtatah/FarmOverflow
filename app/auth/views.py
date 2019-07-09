from . import auth
from flask import redirect,render_template,url_for
from flask_login import login_user,logout_user
from .forms import RegistrationForm,LoginForm
from ..models import User
from ..email import create_mail


@auth.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        full_name = form.full_name.data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        user = User(full_name = full_name, password = password,email = email, username = username)
        user.save_user()
        create_mail("Welcome","email/email",user.email,name = user.full_name)

        return redirect(url_for('auth.login'))

    title = "Register"
    return render_template("auth/register.html", form = form)
