from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     my_dict={'insert_me','Hello I am from views.py'}
#     return render(request,'index.html',context=[])
    # return HttpResponse('insert_me','HELLO')



def index(request):
    context = locals()

    templates = 'firstapp/index.html'

    return render(request, templates, context)