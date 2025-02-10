# from django.conf.urls import url
from django.urls import path
from appn1 import views

app_name = 'appn1'

urlpatterns = [
    path('',views.index, name='home'),
    path('index/', views.index, name= 'index'),
    path('album_list/<int:artist_id>/',views.Album_list, name='album_list'),
    path('album_form/', views.Album_form, name="album_form"),
    path('musician_form/', views.Musician_form, name="musician_form"),
    path('edit_artist/<int:artist_id>/', views.Edit_Artist, name="edit_artist"),
]