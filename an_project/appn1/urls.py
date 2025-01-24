# from django.conf.urls import url
from django.urls import path
from appn1 import views

urlpatterns = [
    path('',views.index, name='index'),
    path('form/', views.form, name='form')
]