from unittest import TestCase
from io import BytesIO
from model import User, Suitcase, SuitcaseItem, IType, Item, Closet, Gender, ICategory, Size, Color, Dress, Top, Pant, connect_to_db, db, sample_data
from server import app


#-----------------------------------------------------------------------------#


class FlaskTestsBasic(TestCase):
    """Flask tests."""

    def setUp(self):
        """Things to do before every test, to provide same environment for every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def test_index(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertIn("Gone the days", result.data)


class FlaskTestsDatabase(TestCase):
    """Flask tests the routes that use the database."""

    def setUp(self):
        """Things to do before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1
        #connect to test database
        connect_to_db(app, "postgresql:///testdb")

        #create tables
        db.create_all()

        #add the sample data
        sample_data()

    def tearDown(self):
        """Done at the end of every test to clear the data"""

        db.session.close()
        db.drop_all()

    def test_register(self):
        """Tests the User Register Page"""

        result = self.client.get("/register")
        self.assertIn("SIGN UP", result.data)

    def test_login_post(self):
        """Tests the User Login Page"""

        result = self.client.post("/login", data={"email": "test@gmail.com", "password:": "test"}, follow_redirects=True)
        self.assertIn("Gone the days", result.data)

    def test_logout(self):
        """Tests the User Logout Page"""

        result = self.client.get("/logout", follow_redirects=True)
        self.assertIn("Logged Out", result.data)

    def test_create_closet_get(self):
        """Tests the Create Closet Page"""

        result = self.client.get("/createcloset")
        self.assertIn("CLOSET NAME:", result.data)

    def test_create_closet_post(self):
        """Tests the create closet page, once closet added"""

        result = self.client.post("/createcloset", data={"closet-name": "Travel", "notes": "travel closet"}, follow_redirects=True)
        self.assertIn("was added", result.data)

    def test_closets(self):
        """Tests all closets page"""

        result = self.client.get("/closets")
        self.assertIn("Travel", result.data)

    def test_view_all_closet_items(self):
        """Tests all closets page"""

        result = self.client.get("/viewcloset/1")
        self.assertIn("Color", result.data)

    def test_add_item(self):
        """Tests the Upload Form Page"""

        result = self.client.get("/addItem")
        self.assertIn("Add Item To A Closet", result.data)

    def test_uploads(self):
        """Tests the Upload Form Page"""

        result = self.client.post("/uploads", data={"file": (BytesIO(b'my file contents'), "/static/images/littleblackdress.jpg"), "color": 1, "closet": 1, "size": 1, "category": 1, "notes": "new", "item-type": "dress"}, follow_redirects=True, content_type='multipart/form-data')
        self.assertIn("Travel", result.data)

    def test_all_items(self):
        """Tests View all items page"""

        result = self.client.get("/allitems")
        self.assertIn("All Items", result.data)

    def test_item_detail(self):
        """Tests item detail page"""

        result = self.client.get("/itemdetail/1")
        self.assertIn("Size:", result.data)

    def test_view_closet(self):
        """Tests the individual view of a closet"""

        result = self.client.get("/viewcloset/1")
        self.assertIn("Travel", result.data)

    def test_add_suitcase(self):
        """Tests the add suitcase"""

        result = self.client.get("/addsuitcase")
        self.assertIn("Keep Calm", result.data)

    def test_add_suitcase_post(self):
        """Tests the process of suitcase being added to db"""

        result = self.client.post("/addsuitcase", data={'suitcase-name': 'Work Trip', 'destination': 'Denver, CO', 'daterange': '10/06/2016 - 10/13/2016', 'notes': 'Pack business casual', 'user_id': 1}, follow_redirects=True)
        self.assertIn("Work Trip", result.data)

    def test_all_suitcases(self):
        """Tests the all suitcases page"""

        result = self.client.get("/allsuitcases")
        self.assertIn("Work Trip", result.data)

    def test_view_suitcase(self):
        """Tests the the page where you can see the contents of a suitcase"""

        result = self.client.get("/viewsuitcase/1")
        self.assertIn("10/06/2016 - 10/13/2016", result.data)

    def test_search(self):
        """Tests the search route"""

        result = self.client.get("/search")
        self.assertIn("items", result.data)

    def test_add_post(self):
        """Tests the adding to suitcase or today"""

        result = self.client.post("/add", data={"suitcase_id": 1, "item_id": 1, "action": "addToSuitcase"})
        self.assertIn("successfully added", result.data)


class FlaskTestsLogins(TestCase):
    """Flask tests the login pages."""
    def setUp(self):
        """Things to do before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True

        #connect to test database
        connect_to_db(app, "postgresql:///testdb")

        #create tables
        db.create_all()

        #add the sample data
        sample_data()

    def tearDown(self):
        """Done at the end of every test to clear the data"""

        db.session.close()
        db.drop_all()

    def test_login(self):
        """Tests the User Login Page"""

        result = self.client.get("/login")
        self.assertIn("LOGIN", result.data)

    def test_register_post(self):
        """Tests the User Register Page uploading to to database"""

        result = self.client.post("/register", data={"first_name": "Noora", "last_name": "Alkowni", "email": "test@gmail.com", "password": "test"}, follow_redirects=True)
        self.assertIn("LOGIN", result.data)
#-----------------------------------------------------------------------------#


if __name__ == "__main__":
    import unittest

    unittest.main()
