"""Models and database functions for Ratings project."""
import datetime
from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()

#-----------------------------------------------------------------------------#
#Model Definitions Aka Tables


class Closet(db.Model):
    """User named closets"""

    __tablename__ = "closets"

    closet_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    closet_name = db.Column(db.String(200), nullable=False)
    notes = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "%s" % (self.closet_name)


class Gender(db.Model):
    """Genders"""

    __tablename__ = "genders"

    gender_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    gender_name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "%s" % (self.gender_name)


class ICategory(db.Model):
    """Possible item catagories user can choose from to organize closet"""

    __tablename__ = "i_categories"

    i_category_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    category_name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "%s" % (self.category_name)


class Size(db.Model):
    """Clothing Sizes"""

    __tablename__ = "sizes"

    size_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    size = db.Column(db.String(65), nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.gender_id'))

    # Define relationship to gender
    gender = db.relationship("Gender",
                           backref=db.backref("sizes"))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "%s" % (self.size)


class Color(db.Model):
    """availble color selection for shoes, bags, accessories"""

    __tablename__ = "colors"

    color_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    color = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "%s" % (self.color)

class Dress(db.Model):
    """User's Dresses database"""

    __tablename__ = "dresses"
    
    dress_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    closet_id = db.Column(db.Integer, db.ForeignKey('closets.closet_id'))
    notes = db.Column(db.String(1000), nullable=False)
    i_category_id = db.Column(db.Integer, db.ForeignKey('i_categories.i_category_id'))
    size_id = db.Column(db.Integer, db.ForeignKey('sizes.size_id'))
    color_id = db.Column(db.Integer, db.ForeignKey('colors.color_id'))
    d_picture = db.Column(db.String, nullable=True)

    # Define relationship to closet
    closet = db.relationship("Closet",
                           backref=db.backref("dresses"))

    # Define relationship to i_category
    i_category = db.relationship("ICategory",
                            backref=db.backref("dresses"))

    # Define relationship to size
    size = db.relationship("Size",
                           backref=db.backref("dresses"))

    # Define relationship to color
    color = db.relationship("Color",
                            backref=db.backref("dresses"))


class Top(db.Model):
    """User's Tops database"""

    __tablename__ = "tops"
    top_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    closet_id = db.Column(db.Integer, db.ForeignKey('closets.closet_id'))
    notes = db.Column(db.String(1000), nullable=False)
    i_category_id = db.Column(db.Integer, db.ForeignKey('i_categories.i_category_id'))
    size_id = db.Column(db.Integer, db.ForeignKey('sizes.size_id'))
    color_id = db.Column(db.Integer, db.ForeignKey('colors.color_id'))

    # Define relationship to closet
    closet = db.relationship("Closet",
                           backref=db.backref("tops"))

    # Define relationship to i_category
    i_category = db.relationship("ICategory",
                            backref=db.backref("tops"))

    # Define relationship to size
    size = db.relationship("Size",
                           backref=db.backref("tops"))

    # Define relationship to color
    color = db.relationship("Color",
                            backref=db.backref("tops"))


class Pant(db.Model):
    """User's Pants database"""

    __tablename__ = "pants"
    pant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    closet_id = db.Column(db.Integer, db.ForeignKey('closets.closet_id'))
    notes = db.Column(db.String(1000), nullable=False)
    i_category_id = db.Column(db.Integer, db.ForeignKey('i_categories.i_category_id'))
    size_id = db.Column(db.Integer, db.ForeignKey('sizes.size_id'))
    color_id = db.Column(db.Integer, db.ForeignKey('colors.color_id'))

    # Define relationship to closet
    closet = db.relationship("Closet",
                           backref=db.backref("pants"))

    # Define relationship to i_category
    i_category = db.relationship("ICategory",
                            backref=db.backref("pants"))

    # Define relationship to size
    size = db.relationship("Size",
                           backref=db.backref("pants"))

    # Define relationship to color
    color = db.relationship("Color",
                            backref=db.backref("pants"))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Pant pant_id=%s i_category_id=%s>" % (self.pant_id, self.i_category)



##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///closets'
#    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."
