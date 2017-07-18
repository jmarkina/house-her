
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#######

class Volunteer(db.Model):
    """this instantiates a volunteer"""

    __tablename__ = "volunteer"

    def __repr__(self):
        return "<Volunteer Name: name=%s Volunteer ID: vol_id=%s>" % (self.name, self.vol_id)


    vol_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    services = db.Column(db.String(100), nullable=False)

class Partners(db.Model): 
    __tablename__ = "partners"

    def __repr__(self):
        return "<Parner Name: part_name=%s Volunteer ID: vol_id=%s>" % (self.part_name, self.part_id)

    part_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    part_name = db.Column(db.String(40), nullable=False)
    cont_name = db.Column(db.String(40), nullable=False)
    cont_email = db.Column(db.String(40), nullable=False)
    cont_phone = db.Column(db.String(20), nullable=False)

class Her(db.Model):



def connect_to_db(app):
    """Connect the database to Flask app."""

    # Configure to use database.
    app.config['SQLALCHEMY_DATABASE_URI'] =  'postgres:///househer'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)





if __name__ == "__main__":
  

    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to househer db."
