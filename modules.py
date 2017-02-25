from app import *
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
