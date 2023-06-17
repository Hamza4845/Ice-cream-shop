from django.http import HttpResponse
from django.shortcuts import render
from myapp1.models import Contact

def hello_view(request):
    return render(request, 'index.html')

    
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Retrieve form data
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        city = request.POST.get('city')

        # Create and save a new contact object
        contact = Contact(fname=fname, lname=lname, phone=phone, city=city)
        contact.save()

        # Render the contact.html template
    return render(request, 'contact.html')


