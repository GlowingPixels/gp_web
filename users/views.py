from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, HttpResponseRedirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserImageChangeForm
from .models import CustomUser

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
def profile(request):
    if request.method == 'POST':
        user_form = CustomUserImageChangeForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            if 'profile_pic' in request.FILES:
                profile_pic = request.FILES['profile_pic']
                user_form.profile_pic = profile_pic
                user_form.save(commit=False)

            if 'cover_pic' in request.FILES:
                cover_pic = request.FILES['cover_pic']
                user_form.cover_pic = cover_pic
                user_form.save(commit=False)
            user_form.save()

            return HttpResponseRedirect(reverse_lazy('users:profile'))

    elif request.method == "GET":
        user_form = CustomUserImageChangeForm(instance=request.user)

        return render(request, 'registration/profile.html', {
            'form': user_form
        })



def settings(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse_lazy('users:profile'))
        else:
            print(user_form.errors)

    elif request.method == "GET":
        user_form = CustomUserChangeForm(instance=request.user)
 
        return render(request, 'registration/settings.html', {
            'form': user_form
        })

# User search Implementation
def search_user(request):
    if request.method == "POST":
        search_text = request.POST["search_text"]
    else:
        search_text = ''
    results = CustomUser.objects.filter(username__icontains=search_text)
    return render(request, 'registration/search_results.html', {
        'search_results': results
        })

def fellow_user(request, fellow_username):
    fellow_user = CustomUser.objects.get(username=fellow_username)
    return render(request, 'registration/fellow_user.html', {'fellow_user': fellow_user})