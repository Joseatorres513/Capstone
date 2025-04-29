from django.shortcuts import render

def store_home(request):
    return render(request, 'online_store/store_home.html')
