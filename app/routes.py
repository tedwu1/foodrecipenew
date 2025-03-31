from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm, RecipeForm
from app.models import User, Recipe
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
@app.route("/recipes")
def home():
    recipes = Recipe.query.all()
    return render_template("recipes.html", recipes=recipes)

@app.route("/recipe/new", methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            author=current_user
        )
        db.session.add(recipe)
        db.session.commit()
        flash("Recipe added successfully!", "success")
        return redirect(url_for('home'))
    return render_template("new_recipe.html", form=form)

@app.route("/recipe/<int:recipe_id>")
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("view_recipe.html", recipe=recipe)
