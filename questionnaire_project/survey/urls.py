from .views import *
from django.urls import path

urlpatterns = [
    path('',Homepage.as_view({
        'get':'list'
    }), name='home'),
    path('login/',LoginView.as_view({
        'post':'create'
    }),name='login'),
    path('survey/',SurveyView.as_view({
        'get':'list',
        'post':'create'
    }),name='survey'),
    path('survey/<int:survey_id>/',SurveyView.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }), name='survey_detail'),
    path('question/',QuestionView.as_view({
        'get':'list',
        'post':'create'
    }),name='question'),
    path('question/<int:question_id>/',QuestionView.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }),name='question_detail'),
    path('activesurveys/',SurveyViewForUser.as_view({
        'get':'list'
    }),name='active_surveys'),
    path('toanswer/<int:survey_id>/',AnswerView.as_view({
        'get':'list',
        'post':'create'
    })),
    path('my_answers/<int:user_id>/',AnswersView.as_view({
        'get':'list'
    }))
]