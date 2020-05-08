# Plexus2.0

### Windows based Setup for Plexus development:
1) Run the following git clone:
 
    `git clone https://github.com/Rohit599/Plexus2.0 Plexus`
    
2) cd into the directory into which you cloned the git repository:
 
    `cd Plexus`
 
3) Run virtualenv on the git cloned directory to setup the Python virtual environment:
 
    `virtualenv env`
 
4) Activate the virtual environment:
 
    `env\scripts\activate`
 
5) After activating the virtual environment, install the dependencies:
 
    `pip install -r requirements.txt`
 
6) Generate initial data by running the command:

    `python manage.py startdata`

7) Now, create the database migrations so as to use the Database:
 
    `python manage.py makemigrations`
    
    `python manage.py migrate`
    
8) Create a supersuperuser:

    `python manage.py createsuperuser`
  
9) You are all set. Run the final command:

    `python manage.py runserver`
    
10) Its time to rock. Visit http://localhost:8000 in your browser and you should be all set.
    
### API Endpoints:

- `admin/` : Opens admin panel
- `api/register/player_register/`: Register a player
- `api/register/society_register/`: Register a society
- `api/register/login/`: Login for player/society
- `api/token/`: Returns an access and refresh JSON web token pair
- `api/token/refresh/`: Returns an access type JSON web token if the refresh token is valid
- `api/events/events/`: Viewset for the event model
- `api/events/events/{pk}/questions`: Viewset for the questions model
- `api/events/rules/`: Viewset for the rules model
- `api/events/past_events/`: Get all past events
- `api/events/present_events/`: Get all present events
- `api/events/future_events/`: Get all future events
- `api/events/leaderboard/<int:pk>`: Leaderboard of a specific event
- `/swagger/`: API Documentation using Swagger
- `/redoc/`: API Documentation using Redoc
