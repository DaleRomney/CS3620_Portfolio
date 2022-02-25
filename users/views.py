from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}. You have successfully created an account.')
            return redirect('login')

    else:
        form = ProfileForm()
    return render(request, 'users/register.html', {'form': form})
