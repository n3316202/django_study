from django.urls import path

from adminInfo import views

urlpatterns = [
    path('', views.index),
    path('<int:member_id>/', views.ajax_adminInfoMain, name='ajax_adminInfoMain'),
    path('<int:member_id>/<int:content_num>/<str:page_label>/', views.ajax_adminInfoContent, name='ajax_adminInfoContent'),
]
