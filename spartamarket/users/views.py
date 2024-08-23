from django.shortcuts import render

# Create your views here.

def profile(request, pk):
    user = request.user
    context = {"user": user}
    return render(request, 'users/profile.html', context)