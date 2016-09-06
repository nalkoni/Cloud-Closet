# Cloud Closet


## Project Description

Gone the days of the closet monster. Say hello to Cloud Closet, a web application that allows users to create and access their closets anywhere. Cloud Closet liberates a user so they can start their day or trip right. It is as simple as signing up, creating a closet and uploading items. Users can also filter their closet by different filter options, check the weather, and add to their consignment closet or their donation closet. Once a user has set up their Cloud Closet they can stop wondering what is inside that dark hole and take advantage of the wasted time in getting dressed or packing a suitcase. Cloud Closet is here to help pinpoint all closet related problems and find a solution to them. 

![homepage](/static/homepage.jpeg?raw=true "Homepage")

Patient Log in:
![Patient login](/static/patientlogin.jpeg?raw=true "Patient Log in page")

Once user is logged in:
![User page](/static/onceuserloggedin.jpeg?raw=true "Once user is logged in")

Schedule view for patient: 
![Schedule view for patient](/static/patientscheduleview.jpeg?raw=true"Schedule view for patient")

Confirmed page:
![Confirmed page](/static/confirmedpage.jpeg?raw=true "Confirmed page")

Provider Log in page:
![Provider log in page](/static/providerloginpage.jpeg?raw=true "Provider Log in page")

Schedule view for the doctor:
![schedule view for the doctor](/static/drsviewofschedule.jpeg?raw=true "Schedule view for the doctor")


## Installation
Appointment App requires a requirements.txt file installation. Appointment App runs through the server.py file on http://localhost:5000/


## API Reference

Travel App runs on a local database. Estimated flight costs and flight booking recommendations are provided by Sambre Api (https://developer.sabre.com/io-docs). Lowest fare for flights is provided by QPX (Google Flights API). Since data is saved locally, Travel app's flight recommendations are based on the departure date Sept 20, 2016 with the booking date as August 10, 2016. 

Data was saved locally to prevent API call expenses, and improve runtime. 

## Tests

Tests for Travel App are located in tests.py . Travel App offers 56% test coverage through unittests. Testing covers assertions on all pages on Travel App, and ensures that when a user selects a city the correct city information is displayed in flight recommendations and event infomation. 

Testing does not cover querying the database, hence the low percentage.

![coverageHTML](/static/coverage.jpg?raw=true "Testing Coverage")

## Tech Stack
Python, Javascript, JQuery, Jinja, SQL, SQLAlchemy, D3, HTML, CSS, Coverage 


