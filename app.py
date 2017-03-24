from __future__ import print_function
import os,sys
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user,current_user


app = Flask(__name__)
app.debug = True

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['postgresql://postgres@localhost/jesse']
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/rpdp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/jesse'
db = SQLAlchemy(app)

# app.register_blueprint(login_py)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)


#registering users into database
class User(UserMixin,db.Model):
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
    def __repr__(self):
        return '<Name %r>' % self.email
    # def is_authenticated():
    #     return True
    # def is_active():
    #     return True
    # def is_anonymous():
    #     return True
    # def getID():
    #     return id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "You have been logged out"

@app.route('/home')
@login_required
def hummus():
    return "The current user is" + current_user.last_name
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
    user = User.query.filter_by(email='jessehuang@wustl.edu ').first()
    print(user.first_name, file=sys.stderr)
    login_user(user)
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

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
