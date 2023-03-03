from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = UserCreationForm()
    context = {'form':form}
    return render(request,'accounts/sign-up.html',context)

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
