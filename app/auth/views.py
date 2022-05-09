from flask import redirect, render_template, url_for

from app.auth.forms import RegistratioForm
from app.models import User
from . import auth
from .. import db


@auth.route('/login')
def login():
    return render_template('auth/login.html')
    

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistratioForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password= form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = 'New Account'
    return render_template('auth/register.html', registration_form = form)