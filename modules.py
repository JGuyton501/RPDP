from app import *

# registering users into database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

    def __init__(
        self, 
        first_name, 
        last_name, 
        email, 
        password
    ):

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
    program_type = db.Column(db.String(80))
    date = db.Column(db.String(30))
    time = db.Column(db.String(10))
    location = db.Column(db.String(80))
    description = db.Column(db.String(500))
    primary_sponsor = db.Column(db.String(30))
    secondary_sponsor = db.Column(db.String(30))
    organizations_involved = db.Column(db.String(30))
    community = db.Column(db.String(30))
    money_spent = db.Column(db.String(30))
    implementation = db.Column(db.String(500))
    improvement = db.Column(db.String(500))
    assessment = db.Column(db.String(500))


    def __init__(
        self, 
        program_name, 
        program_type,
        date, 
        time, 
        location,
        description,
        primary_sponsor,
        secondary_sponsor,
        organizations_involved,
        community,
        money_spent,
        implementation,
        improvement,
        assessment
    ):

        self.program_name = program_name
        self.program_type = program_type
        self.date = date
        self.time = time
        self.location = location
        self.description = description
        self.primary_sponsor = primary_sponsor
        self.secondary_sponsor = secondary_sponsor
        self.organizations_involved = organizations_involved
        self.community = community
        self.money_spent = money_spent
        self.implementation = implementation
        self.improvement = improvement
        self.assessment = assessment

    def __repr__(self):
        return '<Program Name %r>' % self.program_name

# resident 1:1
class OneonOne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resident_first_name = db.Column(db.String(80))
    resident_last_name = db.Column(db.String(80))
    housing = db.Column(db.String(80))
    room_number = db.Column(db.String(10))
    recommended_resources = db.Column(db.String(300))
    concerns = db.Column(db.String(300))
    notes = db.Column(db.String(1000))

    def __init__(
        self, 
        resident_first_name, 
        resident_last_name, 
        housing, 
        room_number,
        recommended_resources,
        concerns,
        notes
    ):

        self.resident_first_name = resident_first_name
        self.resident_last_name = resident_last_name
        self.housing = housing
        self.room_number = room_number
        self.recommended_resources = recommended_resources
        self.concerns = concerns
        self.notes = notes

    def __repr__(self):
        return '<Name %r>' % self.resident_first_name



