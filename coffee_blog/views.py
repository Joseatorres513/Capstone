from django.shortcuts import render

def index(request):
    return render(request, 'coffee_blog/index.html')

def about(request):
    return render(request, 'coffee_blog/about.html')

def contact(request):
    return render(request, 'coffee_blog/contact.html')

def courses(request):
    return render(request, 'coffee_blog/courses.html')
