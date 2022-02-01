from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Request handler
# Request -> response
# action

# Typical uses:
#   Pull data form db
#   Transform
#   Send email

def say_hello(request):
    return render(request, 'hello.html', { 'name': 'Python'})