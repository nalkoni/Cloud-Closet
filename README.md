# Cloud Closet


## Description

Gone the days of the closet monster. Say hello to Cloud Closet, a web application that allows users to create and access their closets anywhere. Cloud Closet liberates a user so they can start their day or trip right. It is as simple as signing up, creating a closet and uploading items. Users can also filter their closet by different filter options, check the weather, and add to their consignment closet or their donation closet. Once a user has set up their Cloud Closet they can stop wondering what is inside that dark hole and take advantage of the wasted time in getting dressed or packing a suitcase. Cloud Closet is here to help pinpoint all closet related problems and find a solution to them.


##Screenshots

####Login
![Login](/static/login.jpg?raw=true "Login Page")

####User Registration 
![User Registration](/static/user_registration.jpg?raw=true "User Registration Page")

####Homepage
<img src="/static/images/homepage.png">

####Adding a Closet
![Add a closet](/static/addcloset.jpg?raw=true "Adding a Closet")

####All Closets
![Add a closet](/static/allclosets.jpeg?raw=true "Once a Closet has been added to database")

####Start Uploading into your Closets
![Uploading Items](static/images/itemupload.jpeg?raw=true"Uploading Items")

####View All Items
![All Items page](/static/allitems.jpeg?raw=true "All Items page")

####Add A Suitcase
![Adding Suitcase page](/static/addsuitcase.jpeg?raw=true "Adding Suitcase page")

####All Suitcases
![All Items page](/static/allsuitcase.jpeg?raw=true "All Suitcases page")



##Technology Stack

- **Application:** Python, Flask, Jinja, SQLAlchemy, PostgreSQL
- **APIs:** WillyWeather
- **Front-End:** HTML/CSS, Bootstrap, JQuery, JavaScript, AJAX

## Testing

Tests for Cloud Closet are located in tests.py. Cloud Closet offers 90% test coverage through unittests.

To run Tests 

```
> python tests.py
```

Happy Testing! 

####Testing Coverage
![coverageHTML](/static/coverage.jpg?raw=true "Testing Coverage")


## How to Run Cloud Closet Locally

Git Pull from https://github.com/nalkoni/Cloud-Closet


Create and Activate a virtual environment 

```
> virtualenv venv
> source venv/bin/activate
```

Install the dependencies

```
> pip install -r requirements.txt
```

Create the Database

```
> createdb closets
```

Run Seed and Model File

```
> python seed.py
> python model.py
```

In Terminal run App
```
> python server.py
```


Open your browser and navigate to 

```
http://localhost:5000/
```

Note: From here you just use Cloud Closet like a user to play around.




### About the Developer    
Noora Alkowni       
[Linkedin](https://www.linkedin.com/in/nooraalkoni)    
 

