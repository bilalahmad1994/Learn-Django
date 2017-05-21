from django.shortcuts import render
from django import forms
from . import forms
# Create your views here.


def index(request):
    return render(request,'firstapp/index.html')

def form_name_view(request):
    form = forms.Formname

    if request.method=='POST':
        form =forms.Formname(request.POST)
        if form.is_valid():
            print('Validation success')
            print('name '+form.cleaned_data['name'])
            print('email ' + form.cleaned_data['email'])
            print('text ' + form.cleaned_data['text'])
    return render(request,'firstapp/form_page.html', {'form': form})

