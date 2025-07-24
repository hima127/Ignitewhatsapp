from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.core.mail import send_mail
from .forms import ContactForm, ReviewForm
from .models import Review
from django.template.loader import render_to_string
from django.contrib import messages
from .models import Job
from .forms import JobApplicationForm

def home(request):
    contact_form = ContactForm()
    review_form = ReviewForm()
    reviews = Review.objects.order_by('-created_at')

    if request.method == "POST":
        if "submit_contact" in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                name = contact_form.cleaned_data["name"]
                email = contact_form.cleaned_data["email"]
                subject_input = contact_form.cleaned_data["subject"]
                phoneno = contact_form.cleaned_data["phoneno"]
                message_input = contact_form.cleaned_data["message"]

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
                    "",  # plain text
                    "user@gmail.com",
                    ["receiver@gmail.com"],
                    html_message=message_html
                )

                messages.success(request, "✅ Your message has been sent successfully!", extra_tags='contact')
                return redirect('home')
            else:
                messages.error(request, "❌ There was an error in the contact form.", extra_tags='contact')

        elif "submit_review" in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review_form.save()
                messages.success(request, "✅ Review submitted successfully.", extra_tags='review')
                return redirect('home')
            else:
                messages.error(request, "❌ There was an error in the review form.", extra_tags='review')

    return render(request, 'chat/index.html', {
        "form": contact_form,
        "review_form": review_form,
        "reviews": reviews
    })



def carriers_view(request):
    jobs = Job.objects.all()
    return render(request, 'chat/carriers.html', {'jobs': jobs})




def apply_job(request, slug):
    job = get_object_or_404(Job, slug=slug)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, "Thank you! Your application has been submitted.")
            return redirect('carriers')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = JobApplicationForm()

    return render(request, 'chat/apply_job.html', {'job': job, 'form': form})