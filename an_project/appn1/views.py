from django.shortcuts import render
from django.http import HttpResponse
from appn1 import models
from appn1 import forms
from django.db.models import Avg


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
    album_list = models.Album.objects.filter(artist = artist_id).order_by('release_date')
    artist_rating = models.Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
    diction = {
        'title': 'List of Albums', 
        'artist_info': artist_info, 
        'album_list':album_list,
        'artist_rating': artist_rating['num_stars__avg'],
    }
    return render(request, 'appn1/album_list.html', context=diction)


# function for album form
def Album_form(request):
    albums_form = forms.AlbumForm()

    if request.method == "POST":
        albums_form = forms.AlbumForm(request.POST)

        if albums_form.is_valid():
            albums_form.save(commit=True)
            return index(request)

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
            return index(request)

    diction = {
        'title':'Add new Musician', 'm_form':musicians_form,
    }
    return render(request, 'appn1/musician_form.html', context=diction)


def Edit_Artist(request, artist_id):
    artist_info = models.Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)

        if form.is_valid():
            form.save(commit=True)
            return Album_list(request, artist_id)

    diction = {
        'form':form,
    }

    return render(request, 'appn1/edit_artist_info.html', context=diction)

def edit_album(request, album_id):
    album_info = models.Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)

    if request.method == "POST":
        form = forms.AlbumForm(request.POST, instance=album_info)

        if form.is_valid():
            form.save(commit=True)

    diction = {
        'form': form
    }

    return render(request, 'appn1/edit_album.html', context=diction)