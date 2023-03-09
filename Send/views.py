from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    send_mail('hello dear cap',
    'hello welcome to this mail',
    ['capchi95@gmail.com'],
    fail_silently=False)
    return render(request,'send/index.html')
