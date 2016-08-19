from model import connect_to_db, db, Gender, ICategory, Size, Color, IType
from server import app

#-----------------------------------------------------------------------------#
#Seeding Functions


def load_genders():
    """Load genders from genders into database"""

    print "Genders"

    for row in open("seed_data/genders"):
        row = row.rstrip()
        gender = row

        gender = Gender(gender_name=gender)

        db.session.add(gender)

    db.session.commit()


def load_sizes():
    """Load sizes from sizes into database"""

    print "Sizes"

    for row in open("seed_data/sizes"):
        row = row.rstrip()
        size, gender_id = row.split("|")

        size = Size(size=size,
                    gender_id=gender_id)

        db.session.add(size)

    db.session.commit()


def load_color():
    "Load colors from colors into database"

    print "Colors"

    for row in open("seed_data/colors"):
        color_name = row.rstrip()

        color_name = Color(color=color_name)

        db.session.add(color_name)

    db.session.commit()


def load_i_categories():
    "Load item categories from i.categories into database"

    print "categories"

    for row in open("seed_data/i.categories"):
        i_category = row.rstrip()

        i_category = ICategory(category_name=i_category)

        db.session.add(i_category)

    db.session.commit()


def load_item_types():
    """Loading the item_types from i.types"""

    print "item_types"

    for row in open("seed_data/i.types"):
        i_type = row.rstrip()

        i_type = IType(type_name=i_type)

        db.session.add(i_type)

    db.session.commit()

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_genders()
    load_sizes()
    load_color()
    load_i_categories()
    load_item_types()
