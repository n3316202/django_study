from django.urls import path
from answer import views

urlpatterns = [
    path('', views.index),
    path('code', views.answer_code,name='answer_code'),
    path('choice', views.answer_choice,name='answer_choice'),
]
