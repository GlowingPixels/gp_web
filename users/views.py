from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def search_user(req):
    if req.method == "POST":
        search_text = req.POST["search_text"]
    else:
        search_text = ''
    results = CustomUser.objects.filter(username__icontains=search_text)
    return render(req, 'registration/search_results.html', {
        'search_results': results
        })