from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from members.forms import SignUpForm

# class view for signup form
# class UserRegistrationView(generic.CreateView):   
#    form_class = SignUpForm
#    template_name = 'registration/signup.html'
#    success_url = reverse_lazy('login')
   
# function view for signup form
def signup_fun(request):
   if request.method == 'POST':
      fm = SignUpForm(request.POST)
      if fm.is_valid():
         # fm.save()
         email = request.POST.get('email')
         password = request.POST.get('password1')
         first_name = request.POST.get('first_name')
         last_name = request.POST.get('last_name')
         username = request.POST.get('username')

         # email already exists
         if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('members:register')
         else:
            user = User(email=email, password=password,  first_name=first_name, last_name=last_name, username=username)
            messages.success(request, 'Signup account Created Successfully!!')
            user.save()
   else:
      fm = SignUpForm ()

   return render(request, 'registration/signup.html', {'form':fm})
