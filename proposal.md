## My Project Proposal

**What I'm building:** I'm building a Flask web app that helps users find the nearest MBTA stop from any place name or address using the Mapbox Geocoding API and the MBTA API and provide information on the air quality at the destination to suggest whether it is a good air quality for users to walk to the train station instead of riding a car.

**Why I chose this:** I chose this project because I constnatly have this concern when traveling in the Boston area without a car. I also wanted to make the project more interesting by adding air quality information because this will remind the users that air pollution is a concern when going into the city.

**Core features:**
- Let the user enter a place name or address in a web form  
- Convert that place into latitude and longitude using the Mapbox API  
- Use the MBTA API to find the nearest transit stop  
- Display the stop name
- Show the air quality at the destination using an air quality API  
- Display the searched location and nearest stop on a map

**What I don't know yet:** 
- How to structure the backend and frontend and link them in a organized way so I don't get confused when coding it
- How to display a Mapbox map inside an HTML template  
- What are the data that are offered by these APIs and how to call for the specific items I need
- How to connect latitude and longitude to the air quality API response  
- How to handle errors cleanly if the user enters an invalid place or if one of the APIs fails