# Cloud <img width=100 src="/static/images/cloud_closet_logo.png"> Closet

####Homepage
<img src="/static/images/homepage.png">


## Description

Gone the days of the closet monster. Say hello to Cloud Closet, a web application that allows users to create and access their closets anywhere. Cloud Closet liberates a user so they can start their day or trip right. It is as simple as signing up, creating a closet and uploading items. Users can also filter their closet by different filter options, check the weather, and add to their consignment closet or their donation closet. Once a user has set up their Cloud Closet they can stop wondering what is inside that dark hole and take advantage of the wasted time in getting dressed or packing a suitcase. Cloud Closet is here to help pinpoint all closet related problems and find a solution to them.

##Technology Stack

- **Application:** Python, Flask, Jinja, SQLAlchemy, PostgreSQL
- **APIs:** WillyWeather
- **Front-End:** HTML/CSS, Bootstrap, JQuery, JavaScript, AJAX


##Screenshots

###Login
<img src="/static/images/login.png">


###User Registration 
<img src="/static/images/register.png">


###Adding a Closet
<img src="/static/images/add_closet.png">


###All Closets
<img src="/static/images/closets.png">


###Start Uploading into your Closets by adding an Item
<img src="/static/images/add_item.png">


###View All Items
-####Male Closet
<img src="/static/images/m_view_all_items.png">
-####Female Closet
<img src="/static/images/f_view_items.png">


###Add A Suitcase
<img src="/static/images/start_suitcase.png">


###All Suitcases
<img src="/static/images/all_suitcases.png">


###Looking inside a suitcase

-####Male Suitcase
<img src="/static/images/m_suitcase.png">

-####Female Suitcase
<img src="/static/images/f_suitcase.png">



##Technology Stack

- **Application:** Python, Flask, Jinja, SQLAlchemy, PostgreSQL
- **APIs:** WillyWeather
- **Front-End:** HTML/CSS, Bootstrap, JQuery, JavaScript, AJAX


## Testing

Tests for Cloud Closet are located in tests.py. Cloud Closet offers ~85% test coverage through unittests.

####Testing Coverage
<img src="/static/images/testing.png">

Happy Testing! 

To run Tests 

```
> python tests.py
```

## How to Run Cloud Closet Locally

Git Pull/Fork from https://github.com/nalkoni/Cloud-Closet


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
 

