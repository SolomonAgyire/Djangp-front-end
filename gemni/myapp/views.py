from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.models  import User, auth
from django.contrib import messages 


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    # Your view logic here
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if user.objects.filter(email =email).exist():
                messages.info(request, 'Email ALready Used')
                return redirect('register')
            elif user.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = user.object.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not the Same')
            return redirect('register')
    else:
        return render(request, 'register.html') 


def login(request):
    if request.methos == 'POST':
        username = request.POST['username']
        password = request.POST[password]

        user = auth.authenticate(username= username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request,  'login.html')

def logout(request):
    auth.logout(request)
