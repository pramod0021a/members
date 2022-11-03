from django.shortcuts import render

# Create your views here.
def index_fun(request):
   return render(request, 'mains/index.html', {})