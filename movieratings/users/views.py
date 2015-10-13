from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        # attempting to log in
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('top_movies')
        else:
            return render(request,
                          'users/login.html',
                          {'failed': True,
                           'username': username})

    return render(request,
                  'users/login.html',
                  {})

# Create your views here.

# def user_register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             password = user.password
#
#             user.set_password(password)
#             user.save()
#
#             profile = Profile(
#                 user=user,
#                 favorite_color='blue',
#             )
#             profile.save()
#
#             user = authenticate(username=user.username,
#                                 password=password)
#             login(request, user)
#             return redirect('recent_statuses')
#     else:
#         form = UserForm()
#     return render(request, 'registration/register.html',
#                   {'form': form})
