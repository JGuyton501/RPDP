import os
from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy
from api.models.testprogram import User

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/rpdptest'
#db = SQLAlchemy(app)


@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()