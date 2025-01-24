from django.shortcuts import render
from django.http import HttpResponse
from appn1.models import Musician, Album
from appn1 import forms


# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by("first_name")
    diction = {
        'filter_test': 'test text',
        'test': 'Musician List: ',
        'musician': musician_list,
    }
    return render(request, 'appn1/index.html', context=diction)

def form(request):
    new_form = forms.MusicianForm

    if request.method=="POST":
        new_form = forms.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
        
    diction = {
        'form': new_form,
        'heading':'Add new Musician'
    }
    return render(request, 'appn1/form.html', context=diction)
