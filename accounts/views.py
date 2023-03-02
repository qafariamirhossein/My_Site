from django.shortcuts import render


def signup_view(request):
    return render(request,'accounts/sign-up.html')

def signin_view(request):
    return render(request,'accounts/sign-in.html')

def logout_view(request):
    return render(request,'accounts/logout.html')