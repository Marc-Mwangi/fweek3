from flask import render_template,redirect ,url_for
from app import app

app.config['SECRET_KEY'] = 'aSKh3r'

# Views
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
    