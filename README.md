# Plexus2.0

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
