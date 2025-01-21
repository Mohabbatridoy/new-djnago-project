from django.shortcuts import render
from django.http import HttpResponse
from appn1.models import Musician, Album
from appn1 import forms


# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by("first_name")

    new_form = forms.user_form()
    diction = {
        'test': 'Musician List: ',
        'musician': musician_list,
        'form': new_form,
        'heading': 'this form is created by Django form'
    }
    return render(request, 'appn1/index.html', context=diction)