from __future__ import print_function
import os,sys
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/rpdptest'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/jesse'
db = SQLAlchemy(app)


# registering users into database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Name %r>' % self.email

 # adding programs
 # change the types later
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String(80))
    location = db.Column(db.String(80))
    date = db.Column(db.String(30))
    time = db.Column(db.String(10))
    description = db.Column(db.String(500))

    def __init__(self, program_name, location, date, time, description):
        self.program_name = program_name
        self.location = location
        self.date = date
        self.time = time
        self.description = description

    def __repr__(self):
        return '<Program Name %r>' % self.location


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submit')
def submit():
    return render_template('submit_program.html')

@app.route('/programs')
def programs():
	allPrograms = Program.query.all()
	return render_template('programs_list.html', allPrograms = allPrograms)

# post new user
@app.route('/post_user', methods=['POST'])
def post_user():
	user = User(
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
    program = Program(
        request.form['program_name'],
        request.form['location'],
        request.form['date'],
        request.form['time'],
        request.form['description']
    )
    db.session.add(program)
    db.session.commit()
    return redirect(url_for('home'))

#check login credentials
@app.route('/post_login', methods=['POST'])
def post_login():
    print('getting to verify_login.', file=sys.stderr)
    form_email = request.form['email']
    form_pass = request.form['password']
    check = User.query.filter(User.email==form_email and User.password==form_pass).first()
    if check is None:
        print('Invalid username or password.',file=sys.stderr)
    else:
        print('Logged in successfully.',file=sys.stderr)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
