import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/postgres'

#import modules after init app 
db = SQLAlchemy(app) 
import modules	

@app.route('/')
def home():
    return render_template('main/home.html')

@app.route('/signup')
def signup():
    return render_template('main/signup.html')

@app.route('/login')
def login():
    return render_template('main/login.html')
	
@app.route('/submit')
def submit():
    return render_template('user/submit_program.html')

# modules below 
# post new user
@app.route('/post_user', methods=['POST'])
def post_user():
	user = modules.User(
		request.form['first_name'],
		request.form['last_name'],
		request.form['email'],
		request.form['password']
		)
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('home'))

# post new program
@app.route('/post_program', methods=['POST'])
def post_program():
	program = modules.Program(
		request.form['program_name'],
		request.form['location'],
		request.form['date'],
		request.form['time'],
		request.form['description']
		)
	db.session.add(program)
	db.session.commit()
	return redirect(url_for('home'))
# query programs 
@app.route('/programs')
def programs():
	allPrograms = modules.Program.query.all()
	return render_template('user/programs_list.html', allPrograms = allPrograms)


if __name__ == '__main__':
    app.run()
