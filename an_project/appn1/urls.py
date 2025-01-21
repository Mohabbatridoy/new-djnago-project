# from django.conf.urls import url
from django.urls import path
from appn1 import views

urlpatterns = [
    path('test/',views.index, name='index'),
]