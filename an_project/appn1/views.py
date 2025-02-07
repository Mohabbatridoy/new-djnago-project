from django.shortcuts import render
from django.http import HttpResponse
from appn1 import models
from appn1 import forms


# Create your views here.
def index(request):
    musicians = models.Musician.objects.order_by('first_name')
    diction = {
        'title':'List of musicians', 'musician':musicians
    }
    return render(request, 'appn1/index.html' , context=diction)


# function for album list
def Album_list(request, artist_id):
    artist_info = models.Musician.objects.get(pk=artist_id)
    album_list = models.Album.objects.filter(artist = artist_id)
    diction = {
        'title': 'List of Albums', 
        'artist_info': artist_info, 
        'album_list':album_list,
    }
    return render(request, 'appn1/album_list.html', context=diction)


# function for album form
def Album_form(request):
    albums_form = forms.AlbumForm()

    if request.method == "POST":
        albums_form = forms.AlbumForm(request.POST)

        if albums_form.is_valid():
            albums_form.save(commit=True)

    diction = {
        'title':'Add new Album', 'a_form': albums_form,
    }
    return render(request,'appn1/album_form.html', context=diction)



# function for musician form
def Musician_form(request):
    musicians_form = forms.MusicianForm()

    if request.method == 'POST':
        musicians_form = forms.MusicianForm(request.POST)

        if musicians_form.is_valid():
            musicians_form.save(commit=True)

    diction = {
        'title':'Add new Musician', 'm_form':musicians_form,
    }
    return render(request, 'appn1/musician_form.html', context=diction)