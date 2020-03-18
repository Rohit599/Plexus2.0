from rest_framework import routers as rest_routers
from django.conf.urls import url, include
from django.urls import path
from rest_framework_nested import routers as nested_routers
from .api import EventViewSet, QuestionViewSet, RuleViewSet, StartEvent, EventDetails, QuestionsPlay, Leaderboard


router = rest_routers.SimpleRouter()
router.register(r'events', EventViewSet)

event_router = nested_routers.NestedSimpleRouter(router, r'events', lookup='event')

event_router.register(r'questions', QuestionViewSet, basename='event-questions')
event_router.register(r'rules', RuleViewSet, basename='event-rules')
# event_router.register(r'leaderboard',Leaderboard, basename='event-leaderboard')

urlpatterns = [
                url(r'^', include(router.urls)),
                url(r'^', include(event_router.urls)),
                path('leaderboard/<int:pk>', Leaderboard.as_view(), name="leaderboard"),
                path('player_dashboard/', StartEvent.as_view(), name="eventList"),
                path('player_dashboard/<int:pk>', EventDetails.as_view(), name="eventDetails"),
                path('player_dashboard/<int:pk>/play', QuestionsPlay.as_view(), name="questions"),

]
