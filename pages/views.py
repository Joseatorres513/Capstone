from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm  # make sure you have this in forms.py

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def experience_view(request):
    return render(request, 'pages/experience.html')  # You’ll need this template

def online_store_view(request):
    return render(request, 'online_store/index.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            message_body = f"This is an email from your portfolio\nName: {name}\nEmail: {email}\nMessage: {message}"

            send_mail(
                "Email from Portfolio",
                message_body,
                email,
                ['tocachu@gmail.com']
            )

            messages.success(request, "Thanks for reaching out! I’ll get back to you soon.")
            return redirect('home')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})

def contact_form_view(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=full_message,
            from_email='your_email@example.com',
            recipient_list=['your_email@example.com'],
        )

        messages.success(request, "Thanks for reaching out! I’ll get back to you soon.")
        return redirect('home')

    return redirect('home')

def testing_view(request):
    return render(request, "pages/test.html")
