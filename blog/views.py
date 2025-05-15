from django.shortcuts import render

def blog_home(request):
    return render(request, 'blog/home.html')

def blog_posts(request):
    return render(request, 'blog/posts.html')

def blog_contact(request):
    return render(request, 'blog/contact.html')
