
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#######

class HHUser(db.Model):
    """this instantiates an HHUser"""

    __tablename__ = "hhuser"
    def __repr__(self):
        return "<HHUser Name: first=%s " % (self.first)

        user_id = 
        first = 
        last = 
        email =
        phone = 
        password =

class HHUsersInfo(db.Model):
    pass



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