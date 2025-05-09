from django.shortcuts import render, redirect
#from .forms import LoginForm
from .models import about, service, data, photo,booking,hero
from django.http import HttpResponse
from collections import defaultdict

def index(request):
    data = about.objects.all().first()
   # port = photo.objects.filter(eventype="Birthday")
   # Picnic = photo.objects.filter(eventype="Picnic")
   # Proposal = photo.objects.filter(eventype="Proposal")
    home = hero.objects.all().first()
    events= photo.objects.all()
    groupevent = defaultdict(list)
    for event in events:
        groupevent[event.eventype].append(event)
    print(groupevent)
    for type,event in groupevent.items():
        print("type:",type)
        for loop in event:
            print(loop.image)
    return render(request,'base.html',{"about":data,"home":home, "grouped_photos":dict(groupevent)})

def services(request):
    serv = service.objects.all()
    home = hero.objects.all().first()
    return render(request, 'service.html',{"service":serv,"home":home})

# def portfolio(request):
    # port = photo.objects.all()
    # print (port)
    # return render(request, 'base.html',{"photo":port})

# def index(request):
    # return render(request,"index.html")
    
def inquery(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        data.objects.create(name=name, email=email, message=message, subject=subject)
        return redirect("index")
    return render(request, 'base.html')

# def book_service(request):
    # if request.method == 'POST':
        # name = request.POST['name']
        # email = request.POST['email']
        # days = request.POST['days']
        # contact = request.POST['contact']
        # service_id = request.POST['service_id']
        # booking.objects.create(name=name, email=email,days=days, contact=contact,service_id=service_id)

        # return ("Booking received! We'll contact you soon.")
    # return redirect('/')

def book_service(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        service_title = request.POST['service_title']
        booking.objects.create(name=name, email=email, contact=contact, service_title=service_title)

        # ✅ Render a confirmation popup-style page
        return render(request, 'booking_success.html')
    return redirect('/')

#########################
