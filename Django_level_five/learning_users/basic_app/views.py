from django.shortcuts import render
from basic_app.forms import Userform,UserProfileInfoForm


#Extra Imports for the Login and Logout capabilities
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required





# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse('You are now Logged in')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered=False

    if request.method =='POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form=Userform(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

        # Hash the password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

        # Set One to One relationship between
        # UserForm and UserProfileInfoForm
            profile.user = user
        # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
            # If yes, then grab it from the POST form reply
                profile.profile_pic=request.FILES['profile_pic']

            #Now save model
            profile.save()

            # Registration Successful!
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=Userform()
        profile_form=UserProfileInfoForm()

    return render(request,'basic_app/registration.html', {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):
    if request.method=='POST':

        # we get the username and password supplied
        username=request.POST.get('username')
        password=request.POST.get('password')


#         Django authentication function
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponse(reverse('index'))
            else:
                return HttpResponseRedirect('Your account is not active')
        else:
            # if you provide for username or password
            print('Someone tried to login ur accout and failed')
            print('They used username:{} and password:{}'.format(username,password))
            return HttpResponse('Invalid Login details')

    else:
        return render(request,'basic_app/login.html',{})












