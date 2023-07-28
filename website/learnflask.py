from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


learnflask = Blueprint('learnflask', __name__)

@learnflask.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    return render_template('login.html')

@learnflask.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == "POST":
        username  = request.form.get("username")
        email  = request.form.get("email")
        password1  = request.form.get("password1")
        password2  = request.form.get("password2")

        if len(username) < 4:
            flash("username must be greater than 4 letters", category='error')
        elif len(password1) < 8:
            flash("passowrd must be atleast 8 letters", category='error')
        elif password1 != password2:
            flash("passwords dont match", category='error')
        else:
            new_user = User(username=username, email=email, password1=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("account created", category='success')
            return redirect(url_for('views.home'))

    return render_template("/signup.html")

