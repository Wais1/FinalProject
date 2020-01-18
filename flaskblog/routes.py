from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
import csv


# Route for the 'home' page. Returns 'home.html' with parameters 'post'.
@app.route("/")
@app.route("/home")
def home():
    global posts
    posts = []
    with open('flaskblog/db.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            posts.append({'username': line[0], 'min_viewers': line[1], 'offer': line[2]})
    return render_template('home.html', posts=posts)


# Route for the 'about' page. Returns 'about.html' with parameters 'title' to customise the title of the page.
@app.route("/about")
def about():
    return render_template('about.html', title='About')


# Route for the 'register' section
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    # If the form is submitted correctly, append the new post to the database
    # and return to 'home' route (front page). Otherwise, load the 'register' template'

    if form.validate_on_submit():
        flash(f'Your post has been created, {form.username.data}!', 'success')
        new_post = {
            'username': form.username.data,
            'min_viewers': form.minimum_viewers.data,
            'offer': form.offer.data,
        }
        with open('flaskblog/db.csv', "a") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            line = form.username.data, form.minimum_viewers.data, form.offer.data
            writer.writerow(line)

        posts.append(new_post)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


# This is a hardcoded version of an authentication system for experimentation.
# Login is only functional with username 'admin@gmail.com' and password 'password'
# The function only displays a successful login message if the login details are successful.

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
