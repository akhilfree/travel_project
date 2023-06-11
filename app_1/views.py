from django.contrib import messages, auth
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import place, head_dept

# Create your views here.

def index(request):
    obj = place.objects.all()
    obj_1 = head_dept.objects.all()
    context = {'obj':obj, 'obj_1':obj_1}
    return render(request, 'index.html', context)

def user_register(request):
    if request.method == 'POST':
        first = request.POST['first_name']
        last = request.POST['last_name']
        mail = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        con = request.POST['con_password']
        if password == con:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, 'Mail Id Already Taken')
            else:
                data = User.objects.create_user(first_name=first, last_name=last, email=mail, username=username,
                                                password=password)
                data.save()
                messages.info(request, 'User Registered Successfully')
                return redirect(login)
        else:
            messages.info(request, 'Password Not Matched')
            return redirect(index)

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(index)
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect(user_register)
    return render(request, 'login.html')


def homepage(request):
    return render(request, 'homepage.html')

def logout(request):
    auth.logout(request)
    return redirect(index)