from django.shortcuts import render
from django import forms
from . import forms
from FormModels.forms import Newuser

# Create your views here.


def index(request):
    return render(request,'firstapp/index.html')

# def form_name_view(request):
#     form = forms.Formname

#     if request.method=='POST':
#         form =forms.Formname(request.POST)
#         if form.is_valid():
#             print('Validation success')
#             print('name '+form.cleaned_data['name'])
#             print('email ' + form.cleaned_data['email'])
#             print('text ' + form.cleaned_data['text'])
#     return render(request ,'firstapp/form_page.html', {'form': form})



# Forms models with meta
def users(request):
    form= Newuser()

    if request.method == 'POST':
        form = Newuser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid')

    return render(request,'firstapp/form_page.html',{'form': form})




