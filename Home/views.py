from django.shortcuts import render, HttpResponse
from django.contrib import messages

from MyAPI.models import UserD

# Create your views here.

def index(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        add_line1 = request.POST.get('add_line1')
        add_line2 = request.POST.get('add_line2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        index = UserD(fname=fname, lname=lname, email=email, phone=phone, add_line1=add_line1, add_line2=add_line2, city=city, state=state, zipcode=zipcode)
        index.save()
        messages.success(request, 'Your contact details have been saved.')

    return render(request, 'index.html')
