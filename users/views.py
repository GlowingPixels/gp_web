from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from .forms import CustomUserCreationForm
from .models import CustomUser

#User SignUp
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# User search Implementation
def search_user(req):
    if req.method == "POST":
        search_text = req.POST["search_text"]
    else:
        search_text = ''
    results = CustomUser.objects.filter(username__icontains=search_text)
    return render(req, 'registration/search_results.html', {
        'search_results': results
        })

def fellow_user(req, fellow_username):
    fellow_user = CustomUser.objects.get(username=fellow_username)
    return render(req, 'registration/fellow_user.html', {'fellow_user': fellow_user})