from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.template.loader import render_to_string
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject_input = request.POST.get("subject")
        phoneno = request.POST.get("phoneno")
        message_input = request.POST.get("message")

        if form.is_valid():
            sendemail = "himasok2020@gmail.com"  # Replace with your receiving email

            subject = "You Got an Enquiry in IgniteWhatsapp"
            message_html = render_to_string("chat/contactmail.html", {
                "name": name,
                "email": email,
                "phoneno": phoneno,
                "subject": subject_input,
                "message": message_input
            })

            send_mail(
                subject,
                "",  # Plain text fallback (optional)
                "himasok2020@gmail.com",  # Sender
                [sendemail],             # Receiver
                html_message=message_html
            )

            messages.success(request, "Your message has been sent successfully!")
            return render(request, "chat/index.html", {"form": ContactForm()})
        else:
            messages.error(request, "There was an error in the form. Please try again.")
            return render(request, "chat/index.html", {"form": form})

    return render(request, 'chat/index.html', {"form": ContactForm()})
