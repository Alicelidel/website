# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('<center><h2>Hello World from me</h2></center>')