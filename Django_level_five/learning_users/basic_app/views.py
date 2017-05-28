from django.shortcuts import render
from basic_app.forms import Userform,UserProfileInfoForm



# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')


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










