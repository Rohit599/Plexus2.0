from rest_framework import routers as rest_routers
from django.conf.urls import url, include
from rest_framework_nested import routers as nested_routers

from .api import EventViewSet, QuestionViewSet, ScoreViewSet, RuleViewSet

router = rest_routers.DefaultRouter()
router.register('events', EventViewSet, 'events')   
router.register('scores', ScoreViewSet, 'scores')
router.register('rules', RuleViewSet, 'rules')

question_router = nested_routers.NestedSimpleRouter(router, 'events', lookup='events')
question_router.register('questions', QuestionViewSet, 'questions')


urlpatterns = [
		    url(r'^', include(router.urls)),
		    url(r'^', include(question_router.urls)),
]