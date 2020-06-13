from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth #권한

def signup(request):
    #계정 만들기
    if request.method == 'POST':
        if request.POST['pw1'] == request.POST['pw2']:
            user = User.objects.create_user(username=request.POST['name'], password=request.POST['pw1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pw']
        user = auth.authenticate(request, username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')