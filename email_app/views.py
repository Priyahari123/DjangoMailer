from django.shortcuts import render
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse
import json
from django.http.response import JsonResponse



# Create your views here.

def home(request):
    return render(request,"email_template.html")


def email_send(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        name = request.POST.get('name', None)
        content = request.POST.get('content', None)
        subject = request.POST.get('subject', None)
        print(email, "email")
        your_email='youremail@gmail.com'

        # inject the respective values in HTML template
        html_message = loader.render_to_string(
            'email_message.html',
            {
                # TODO: Enter the recipient name
                'name': name,
                # TODO:  Update with your own body
                'body': content,
                # TODO: Update the signature
                'sign': 'Haripriya C',
            })
        send_mail(
            subject,
            'You are lucky to receive this mail.',
            your_email,  # : Update this with your mail id
            [email],  # : Update this with the recipients mail id
            html_message=html_message,
            fail_silently=False,
        )
        return JsonResponse({'status': 'success'})
