from django.urls import path, include
from rest_framework import routers
from .views import (
    SurveyViewSet, QuestionViewSet, ChoiceViewSet,
    CreateAnswerViewSet, ActiveSurveyListViewSet,
    UserSurveyListViewSet,
)
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

v1_router = routers.DefaultRouter()
v1_router.register('surveys', SurveyViewSet, basename='survey')
v1_router.register(
    'surveys/(?P<survey_id>.+)/questions',
    QuestionViewSet,
    basename='question'
)
v1_router.register(
    'surveys/(?P<survey_id>.+)/questions/(?P<question_id>.+)/choices',
    ChoiceViewSet,
    basename='choice'
)
v1_router.register(
    'surveys/(?P<survey_id>.+)/questions/(?P<question_id>.+)/answers',
    CreateAnswerViewSet,
    basename='answer'
)
v1_router.register(
    'active',
    ActiveSurveyListViewSet,
    basename='active'
)
v1_router.register(
    'passed',
    UserSurveyListViewSet,
    basename='passed'
)

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(v1_router.urls))
]
