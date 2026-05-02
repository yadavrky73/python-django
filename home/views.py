from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from home.models import Contact
# from django.contrib import messages


def index(request):
    context = {
        'variable': "this is Krishna's home and i am his child",
        'variable1': "this is Krishna's home and i am servent of his"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        # Extract form fields exactly as they appear in your contact.html
        name = request.POST.get('name')
       # last_name = request.POST.get('last_name')
        email = request.POST.get('email')
       # phone = request.POST.get('phone')          # optional, model will ignore if no field
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Combine name
       # full_name = f"{first_name} {last_name}".strip()

        # Create and save contact (without 'date' argument)
        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message,
            # phone field not in model – we'll handle separately (see model update below)
        )
        contact.save()

        # Success message and redirect
        messages.success(request, "Thank you! Your message has been sent. Hare Krishna 🙏")
        # messages.success(request, "Profile details updated.")

        return redirect('contact')   # redirect to same page to avoid re-POST

    # GET request – just show the empty form
    return render(request, 'contact.html')