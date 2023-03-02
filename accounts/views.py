from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout

def signup_view(request):
    return render(request,'accounts/sign-up.html')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')        

    return render(request,'accounts/sign-in.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
