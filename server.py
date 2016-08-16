"""closet application"""
import os
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, url_for, session, send_from_directory
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename

from model import connect_to_db, db, ICategory, Closet, Gender, Size, Color, Dress, Top, Pant

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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():

    return render_template("homepage.html")


@app.route('/addItem', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print "File:%s" % (file)
        # if user does not select file, browser also
        # submit a empty part without filename

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    

    colors = Color.query.order_by('color').all()
    closets = Closet.query.order_by('closet_name').all()
    i_categories = ICategory.query.order_by('category_name').all()
    sizes = Size.query.filter(Size.gender_id == 2).all()
                                                    
    return render_template("add_item.html",
                            colors=colors,
                            closets=closets,
                            sizes=sizes,
                            i_categories=i_categories)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # print filename create a html template show image, have all of the form stuff anything i want user to fill out send it normal way and then send the filename to the datebase 

    return render_template("closet.html")


@app.route('/createcloset', methods=['GET'])
def create_closet():
    """Creating a new user closet to add to database"""

    return render_template("add_closet_form.html")


@app.route('/createcloset', methods=['POST'])
def closet_created():
    """adding the closet to the database"""

    closet_name = request.form["closet-name"]
    notes = request.form["notes"]

    new_closet = Closet(closet_name=closet_name, notes=notes)

    db.session.add(new_closet)
    db.session.commit()

    flash("%s Closet was added." % closet_name)

    return redirect("/")



@app.route('/closets')
def all_closets():
    """All closets"""

    closets = Closet.query.order_by(Closet.closet_name).all()


    return render_template("closets.html",
                            closets=closets) #in the templates im calling closets closets 


@app.route('/viewcloset/<int:closet_id>', methods=['GET'])
def view_all_closet_items(closet_id):
    """Displays all items in closet"""
    # user clicked closet
    dresses = Dress.query.filter(Dress.closet_id == closet_id).all()
    tops = Top.query.filter(Top.closet_id == closet_id).all()
    pants = Pant.query.filter(Pant.closet_id == closet_id).all()

    return render_template("view_closet.html",
                            dresses=dresses,
                            tops=tops,
                            pants=pants)

@app.route('/closetitem', )
def view_closet_item():
    """When user clicks closet item it displays more information"""
    # item_clicked =  request.form[" "]

    # dresses = Dress.query.filter(Dress.) 
    # tops = Top.query.filter(Top.)
    # pants =  Pant.query.filter(Pant.)   
    # movie = Movie.query.get(movie_id)



    return render_template("closet_item.html")





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")