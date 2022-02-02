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

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', { 'name': 'Python'})