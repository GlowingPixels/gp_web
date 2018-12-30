from django.shortcuts import render
from django.urls import reverse
from .forms import UserForm, UserProfileForm
from .models import User, UserProfile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

def user_signup(req):

    registered = False

    if(req.method == "POST"):

        user_form = UserForm(data=req.POST)
        profile_form = UserProfileForm(data=req.POST)

        if(user_form.is_valid() and profile_form.is_valid()):

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']
            
            profile.save()
            registered = True
            username = req.POST['username']
            password = req.POST['password']
            #authenticate user then login
            user = authenticate(username=username, password=password)
            login(req, user)


        else:
            print (user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(req, 'users/signup.html', {
        "registered": registered,
        "user_form": user_form,
        "profile_form": profile_form,
    })

def user_login(req):
    if(req.method == "POST"):
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if(user.is_active):
                login(req, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("Account Deactivated")
        else:
            return render(req, 'users/login.html', {
                'failed': True
                })
    else:
            return render(req, 'users/login.html', {
                'failed': False
                })

@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('index'))

@login_required
def user_info(req):
    user_data = req.user
    return render(req, 'users/user_info.html', {
        'user_data':user_data
        })