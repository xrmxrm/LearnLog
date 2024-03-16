from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Not a POST. Pretend it's a GET. Blank reg form
        form = UserCreationForm()
    else:
        # POST: process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display the form (blank or invalid)
    context = {'form': form}
    return render(request, 'registration/register.html', context)


