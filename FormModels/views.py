from django.shortcuts import render
from . import forms
# Create your views here.


def index(request):
    return render(request,'firstapp/index.html')

def form_name_view(request):
    form=forms.Formname()
    return render(request, 'firstapp/form_page.html', {'form': form})

