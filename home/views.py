from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name, email=email, message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        # return render(request, 'thankyou.html')
    return render(request, 'contact.html')