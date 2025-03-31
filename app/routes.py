from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user  # Add login_required here
from app import app, db
from app.forms import LoginForm, RecipeForm
from app.models import User, Recipe
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template('login.html', form=form)
