from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def contactPage(request):
    result = None
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Compose the email
        subject = f"New Contact Form Message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_list = [settings.EMAIL_HOST_USER]  # Your email address

        try:
            # Send the email
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False,
            )
            result = "Thank you! Your message has been sent successfully."
        except Exception as e:
            result = f"Oops! Something went wrong: {str(e)}"

    return render(request, "contact.html", {"result": result})
