from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Forum Home</h1>')
# Create your views here.

def about(request):
    return HttpResponse('<h1>About us</h1>')