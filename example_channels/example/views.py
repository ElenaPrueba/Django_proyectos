from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def user_list(request):
    return render(request, 'example/user_list.html')
