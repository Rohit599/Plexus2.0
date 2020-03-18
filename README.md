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
- `api/events/events/<int:pk>/questions/<int:pk>`
- `api/events/events/{pk}/rules`: Viewset for the rules model
- `api/events/events/{pk}/rules/{pk}`
- `api/events/player_dashboard`: ListAPIView for all the events
- `api/events/player_dashboard/<int:pk>`: Details of the event
- `api/events/player_dashboard/<int:pk>/play`: Questions for the event
