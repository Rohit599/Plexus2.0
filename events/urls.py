from rest_framework import routers as rest_routers
from django.conf.urls import url, include
from django.urls import path
from rest_framework_nested import routers as nested_routers
from .api import EventViewSet, QuestionViewSet, RuleViewSet, StartEvent, EventDetails, QuestionsPlay, Leaderboard, PastEventsView, PresentEventsView, FutureEventsView


router = rest_routers.SimpleRouter()
router.register(r'events', EventViewSet)

event_router = nested_routers.NestedSimpleRouter(
    router, r'events', lookup='event')

event_router.register(
    r'questions',
    QuestionViewSet,
    basename='event-questions')
event_router.register(r'rules', RuleViewSet, basename='event-rules')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(event_router.urls)),
    path('past_events/', PastEventsView.as_view(), name="past-events"),
    path('present_events/', PresentEventsView.as_view(), name="present-events"),
    path('future_events/', FutureEventsView.as_view(), name="future-events"),
    path('leaderboard/<int:pk>', Leaderboard.as_view(), name="leaderboard"),
    path('player_dashboard/', StartEvent.as_view(), name="eventList"),
    path('player_dashboard/<int:pk>', EventDetails.as_view(), name="eventDetails"),
    path('player_dashboard/<int:pk>/play', QuestionsPlay.as_view(), name="questions"),

]
