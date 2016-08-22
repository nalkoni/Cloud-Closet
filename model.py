"""Models and database functions for Ratings project."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

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


class IType(db.Model):
    """ Types of Items in Closet"""

    __tablename__ = "i_types"

    i_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "%s" % (self.type_name)


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


class Item(db.Model):
    """ User's Items in Closet"""

    __tablename__ = "items"

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    i_type_id = db.Column(db.Integer, db.ForeignKey('i_types.i_type_id'))
    closet_id = db.Column(db.Integer, db.ForeignKey('closets.closet_id'))
    notes = db.Column(db.String(1000), nullable=False)
    i_category_id = db.Column(db.Integer, db.ForeignKey('i_categories.i_category_id'))
    size_id = db.Column(db.Integer, db.ForeignKey('sizes.size_id'))
    color_id = db.Column(db.Integer, db.ForeignKey('colors.color_id'))
    image_filepath = db.Column(db.String, nullable=True)

    # Define relationship to closet
    closet = db.relationship("Closet",
                             backref=db.backref("items"))

    # Defines relationship to i_types
    i_type = db.relationship("IType",
                             backref=db.backref("items"))

    # Define relationship to i_category
    i_category = db.relationship("ICategory",
                                 backref=db.backref("items"))

    # Define relationship to size
    size = db.relationship("Size",
                           backref=db.backref("items"))

    # Define relationship to color
    color = db.relationship("Color",
                            backref=db.backref("items"))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "%d" % (self.item_id)


class Dress(db.Model):
    """User's Dresses database"""

    __tablename__ = "dresses"

    dress_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))

    item = db.relationship("Item",
                           backref=db.backref("dresses"))


class Top(db.Model):
    """User's Tops database"""

    __tablename__ = "tops"

    top_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))

    item = db.relationship("Item",
                           backref=db.backref("tops"))


class Pant(db.Model):
    """User's Pants database"""

    __tablename__ = "pants"

    pant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))

    item = db.relationship("Item",
                           backref=db.backref("pants"))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Pant pant_id=%s>" % (self.pant)

#------------------------------------------------------------------------------#
#Testing Data


def sample_data():
    """sample data for testing"""

    #add sample data to above Classes(tables)
    ct = Closet(closet_name='Travel', notes='travel closet')
    cs = Closet(closet_name='Random', notes='random closet')
    db.session.flush()

    idress = IType(type_name='Dress')
    itop = IType(type_name='Top')
    ipant = IType(type_name='Pant')
    db.session.flush()

    gf = Gender(gender_name='female')
    db.session.flush()

    icb = ICategory(category_name='business/work')
    icf = ICategory(category_name='formal')
    db.session.flush()

    sxs = Size(size='Regular XXS-XS (00-2)', gender_id=1)
    sm = Size(size='Regular M (8-10)', gender_id=1)
    db.session.flush()

    cb = Color(color='blue')
    cr = Color(color='red')
    db.session.flush()

    new_item_dress = Item(i_type_id=1, closet_id=1,  notes='New dress, possibly for interview', i_category_id=1, size_id=1, color_id=1, image_filepath='/static/images/littleblackdress.jpg')
    new_item_top = Item(i_type_id=2, closet_id=2, notes='New top, possibly for interview', i_category_id=2, size_id=2, color_id=2, image_filepath='/static/images/littleblackdress.jpg')
    new_item_pant = Item(i_type_id=3, closet_id=1, notes='New pants, possibly for interview', i_category_id=1, size_id=1, color_id=1, image_filepath='/static/images/littleblackdress.jpg')
    db.session.flush()

    new_dress = Dress(item_id=1)
    new_top = Top(item_id=2)
    new_pant = Pant(item_id=3)
    db.session.flush()

    db.session.add_all([ct, cs, idress, itop, ipant, gf, icb, icf, sxs, sm, cb, cr, new_item_dress, new_item_top, new_item_pant, new_dress, new_top, new_pant])
    db.session.commit()


##############################################################################
# Helper functions

def connect_to_db(app, db_uri="postgresql:///closets"):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
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
