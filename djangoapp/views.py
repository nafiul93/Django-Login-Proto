# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Perform authentication (you can replace this with your authentication logic)

        # For demonstration purposes, let's just check if the username is "admin" and password is "password"
        if username == 'admin' and password == 'password':
            return HttpResponse('Login successful!')
        else:
            return HttpResponse('Login failed. Please check your username and password.')

    return render(request, 'login.html')
