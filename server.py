"""closet application"""
import os
from jinja2 import StrictUndefined
from sqlalchemy import func

from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename
from flask_wtf import Form
from wtforms.fields.html5 import DateField


from model import connect_to_db, db, User, ICategory, Closet, IType, Gender, Size, Color, Item, Dress, Top, Pant, Suitcase, SuitcaseItem

#file  path to store the uploaded files
UPLOAD_FOLDER = 'static/images'
#the set of allowed file extentions, so user won't be able to upload everything
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'JPG'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Required to use Flask sessions and the debug toolbar
app.secret_key = "organized"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. This is so instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


#-----------------------------------------------------------------------------#
#Routes

class ExampleForm(Form):
    """docstring for ExampleForm"""

    dt = DateField('DatePicker', format='%Y-%m-%d')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """homepage"""

    if 'user_id' in session:
        return render_template("homepage.html")
    else:
        flash('Please Login!')
        return redirect('login')


@app.route('/register', methods=['GET'])
def register():
    """Display User Registration Form"""

    return render_template("user_register.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Display User Registration Form"""

    f_name = request.form.get('first_name')
    l_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    new_user = User(first_name=f_name,
                    last_name=l_name,
                    email=email,
                    password=password)

    db.session.add(new_user)
    db.session.commit()

    return redirect("login")


@app.route('/login', methods=['GET'])
def login():
    """Display Login Form"""

    if 'user_id' in session:
        return render_template("homepage.html")
    else:
        flash('Please Login!')
        return render_template("login_form.html")


@app.route('/login', methods=['POST'])
def login_validation():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("Invalid Email, Please Try Again")
        return redirect("login")

    if user.password != password:
        flash("Invalid Password, Please Try Again")
        return redirect("login")

    session['user_id'] = user.user_id

    flash("Logged In!")
    return redirect("/")


@app.route('/logout')
def logout():
    del session["user_id"]
    flash('Logged Out')
    return redirect(url_for('login'))


@app.route('/createcloset', methods=['GET'])
def create_closet():
    """Creating a new user closet to add to database"""

    if 'user_id' in session:
        return render_template("add_closet_form.html")
    else:
        flash('Please Login')
        return redirect('login')


@app.route('/createcloset', methods=['POST'])
def closet_created():
    """adding the closet to the database"""

    closet_name = request.form.get("closet-name")
    notes = request.form.get("notes")
    user_id = session.get('user_id')
    print ("User_ID: %s" % user_id)

    new_closet = Closet(closet_name=closet_name, notes=notes, user_id=user_id)

    db.session.add(new_closet)
    db.session.commit()

    flash("%s Closet was added." % closet_name)

    return redirect("/closets")


@app.route('/closets')
def all_closets():
    """All closets"""

    user_id = session.get('user_id')

    closets = Closet.query.filter_by(user_id=user_id).order_by(Closet.closet_name).all()

    return render_template("closets.html",
                           closets=closets)
    #in the templates im calling closets closets


@app.route('/viewcloset/<int:closet_id>', methods=['GET'])
def view_all_closet_items(closet_id):
    """Displays all items in closet"""

    user_id = session.get('user_id')

    colors = Color.query.all()

    categories = ICategory.query.all()

    closet = Closet.query.filter(Closet.closet_id == closet_id).one()

    suitcases = Suitcase.query.filter(Suitcase.user_id == user_id).all()

    # user clicked closet
    items = Item.query.filter((Item.closet_id == closet_id) & (Item.user_id == user_id)).all()

    return render_template("view_closet.html",
                           colors=colors,
                           categories=categories,
                           closet=closet,
                           suitcases=suitcases,
                           items=items)


@app.route('/addItem')
def upload_file():
    """Form to enter item into closet"""

    colors = Color.query.order_by('color').all()
    closets = Closet.query.order_by('closet_name').all()
    i_categories = ICategory.query.order_by('category_name').all()
    item_types = IType.query.order_by('type_name').all()
    sizes = Size.query.filter(Size.gender_id == 2).all()
    user_id = session.get('user_id')

    return render_template("add_item.html",
                           colors=colors,
                           closets=closets,
                           item_types=item_types,
                           i_categories=i_categories,
                           sizes=sizes,
                           user_id=user_id)


@app.route('/uploads', methods=['POST'])
def uploaded_file():
    """Inputs item into closets databases"""

    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        # return redirect(request.url)

    uploaded_file = request.files.get('file')
    # if user does not select file, browser also
    # submit a empty part without filename

    if uploaded_file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    image_path = "/static/images/" + filename
    color = request.form.get('color')
    closet = request.form.get('closet')
    size = request.form.get('size')
    category = request.form.get('category')
    notes = request.form.get('notes')
    item_type = request.form.get('item_type')
    user_id = session.get('user_id')

    #Handle case for when item_type is pant
    if item_type == '1':
        new_item_pants = Item(user_id=user_id, i_type_id=item_type, closet_id=closet, notes=notes, i_category_id=category, size_id=size, color_id=color, image_filepath=image_path)
        db.session.flush()

        result = db.session.query(func.max(Item.item_id)).one()
        max_id = result
        new_pants = Pant(item_id=max_id)

        db.session.add_all([new_item_pants, new_pants])
        db.session.commit()

    #Handle case for when item_type is dress
    if item_type == '2':
        new_item_dress = Item(user_id=user_id, i_type_id=item_type, closet_id=closet, notes=notes, i_category_id=category, size_id=size, color_id=color, image_filepath=image_path)
        db.session.flush()

        result = db.session.query(func.max(Item.item_id)).one()
        max_id = result
        new_dress = Dress(item_id=max_id)

        db.session.add_all([new_item_dress, new_dress])
        db.session.commit()

    #Handle case for when item_type is top
    if item_type == '3':
        new_item_top = Item(user_id=user_id, i_type_id=item_type, closet_id=closet, notes=notes, i_category_id=category, size_id=size, color_id=color, image_filepath=image_path)
        db.session.flush()

        result = db.session.query(func.max(Item.item_id)).one()
        max_id = result
        new_top = Top(item_id=max_id)

        db.session.add_all([new_item_top, new_top])
        db.session.commit()

    return redirect("/closets")


@app.route('/allitems', methods=['GET'])
def view_all_items():
    """User has option to view all uploaded items regardless of closet"""

    user_id = session.get('user_id')

    colors = Color.query.all()

    categories = ICategory.query.all()

    suitcases = Suitcase.query.filter(Suitcase.user_id == user_id).all()

    closets = Closet.query.filter(Closet.user_id == user_id).all()

    items = Item.query.filter(User.user_id == user_id).all()

    return render_template("view_all_items.html",
                           items=items,
                           colors=colors,
                           categories=categories,
                           closets=closets,
                           suitcases=suitcases)


@app.route('/add', methods=['POST'])
def adding_to_suitcase_or_today():
    """Adding to a suitcase_items table or to wear today"""

    user_id = session.get('user_id')
    suitcase_id = request.form.get("suitcase_id")
    item_id = request.form.get("item_id")

    action = request.form.get("action")
  
    if action == "addToSuitcase":
        suitcase_item = SuitcaseItem(suitcase_id=suitcase_id, item_id=item_id)
        alert = "You have successfully added this  to your suitcase!"

        db.session.add(suitcase_item)
        db.session.commit()
    else:
        alert = "Action not allowed"

    return jsonify({'alert': alert})


@app.route('/itemdetail/<int:item_id>', methods=['GET'])
def view_closet_item(item_id):
    """When user clicks closet item it displays more information"""

    item = Item.query.get(item_id)

    return render_template("item_detail.html",
                           item=item)


@app.route('/addsuitcase', methods=['GET'])
def add_suitcase():
    """Allows user to start a suitcases"""

    return render_template("add_suitcase_form.html")


@app.route('/addsuitcase', methods=['POST'])
def add_suitcase_to_database():
    """Allows user to create closet"""

    suitcase_name = request.form.get("suitcase-name")
    destination = request.form.get("destination")
    daterange = request.form.get("daterange")
    notes = request.form.get("notes")
    user_id = session.get('user_id')

    new_suitcase = Suitcase(suitcase_name=suitcase_name, destination=destination, travel_dates=daterange, notes=notes, user_id=user_id)

    db.session.add(new_suitcase)
    db.session.commit()


    return redirect("/allsuitcases")


@app.route('/allsuitcases', methods=['GET'])
def all_suitcases():
    """User can see all suitcases"""

    user_id = session.get('user_id')

    suitcases = Suitcase.query.filter_by(user_id=user_id).order_by(Suitcase.suitcase_name).all()

    return render_template("suitcases.html",
                           suitcases=suitcases)


@app.route('/viewsuitcase/<int:suitcase_id>', methods=['GET'])
def view_suitcases(suitcase_id):
    """User can see all items and suitcase information in their suitcase"""

    user_id = session.get('user_id')

    suitcase = Suitcase.query.get(suitcase_id)

    items = Item.query.filter(Item.user_id == user_id).all()

    # suitcase = Suitcase.query.filter((Suitcase.suitcase_id == suitcase_id) & (Suitcase.user_id == user_id)).one()

    suitcase_items = SuitcaseItem.query.filter(SuitcaseItem.suitcase_id == suitcase_id).all()

    return render_template("suitcase_view.html",
                           suitcase=suitcase,
                           suitcase_items=suitcase_items,
                           items=items)


@app.route('/search', methods=['GET'])
def search_items():
    """ Allows user to search using parameters """

    color = request.args.get('color')
    category = request.args.get('category')
    size = request.args.get('size')
    closet = request.args.get('closet')

    print color
    criteria = []

    if color:  # if color is not None:
        criteria.append(Item.color_id == color)

    if category:
        criteria.append(Item.i_category_id == category)

    if size:
        criteria.append(Item.size_id == size)

    if closet:
        criteria.append(Item.closet_id == closet)

    items = Item.query.filter(*criteria).all()

    item_ids = []

    for item in items:
        item_ids.append(str(item.item_id))

    return jsonify(items=item_ids)


#-----------------------------------------------------------------------------#
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")