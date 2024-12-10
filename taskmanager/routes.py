from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")

@app.route("/categories")
def categories():
    # pass the categories to the template as a cursor object, so use list() to convert it to a list
    categories = list(Category.query.order_by(Category.category_name).all()) # get all categories from the database and order them by category name
    return render_template("categories.html", categories=categories) # first categories is the name of the variable in the template, the second categories is the variable in this function

@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name = request.form.get("category_name"))# name in the model must match the name in the form
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    
    return render_template("add_category.html")

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)