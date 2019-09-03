from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    """
    If we get a POST request there will be form data, so try and validate
    data.
    If we get a GET request there will be no data so just display empty form.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Hashes the password and creates the user
            username = form.cleaned_data.get('username')
            messages.success(request, "Your accoutn has been created! You are now able to login.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form' : form})    


@login_required
def profile(request):
    return render(request, 'users/profile.html')