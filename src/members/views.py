from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from members.forms import SignUpForm

# Create your views here.
class UserRegistrationView(generic.CreateView):
   # form_class = UserCreationForm
   form_class = SignUpForm
   template_name = 'registration/signup.html'
   success_url = reverse_lazy('login')
