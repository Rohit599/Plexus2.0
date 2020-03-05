from rest_framework import routers
from .api import EventViewSet, QuestionViewSet, ScoreViewSet, RuleViewSet

router = routers.DefaultRouter()
router.register('list', EventViewSet, 'events')
router.register('questions', QuestionViewSet, 'questions')
# router.register('answers', AnswerViewSet, 'answers')
router.register('scores', ScoreViewSet, 'scores')
router.register('rules', RuleViewSet, 'rules')

urlpatterns = router.urls