from django.shortcuts import render

def blog_home(request):
    return render(request, 'blog/blog_home.html')

def blog_posts(request):
    return render(request, 'blog/blog_posts.html')

def blog_contact(request):
    return render(request, 'blog/blog_about.html')
