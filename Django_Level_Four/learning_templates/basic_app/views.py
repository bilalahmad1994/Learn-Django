from django.shortcuts import render

# Create your views here.
def index(request):
    context_dic={'text':'helloworld','number':99}
    return render(request,'basic_app/index.html',context_dic)

def other(request):
    return render(request,'basic_app/login.html')

def relative(request):
    return render(request,'basic_app/registration.html')
