from django.shortcuts import render, redirect
#from .forms import LoginForm
from .models import about, service, data, photo,booking,hero, PopupImage, Gallery,Ourstory,Whatsapp
from django.http import HttpResponse
from collections import defaultdict
from django.core.paginator import Paginator

def index(request):
    data = about.objects.all().first()
   # port = photo.objects.filter(eventype="Birthday")
   # Picnic = photo.objects.filter(eventype="Picnic")
   # Proposal = photo.objects.filter(eventype="Proposal")
    home = hero.objects.all().first()
    events= photo.objects.all()
    ourstory = Ourstory.objects.all()

    groupevent = defaultdict(list)

    for event in events:
        groupevent[event.eventype].append(event)
    print(groupevent)
    group = dict(groupevent)
    paginator = Paginator(list(group.items()),7)
    pagenumber = request.GET.get("page",1)
    print(pagenumber)
    page_objects = paginator.get_page(pagenumber)
    print(page_objects)
    print(group)
    popup = PopupImage.objects.filter(is_active=True).order_by('-updated_at').first()
    app = Whatsapp.objects.all().first
    # for type,event in groupevent.items():
        # print("type:",type)
        # for loop in event:
            # print(loop.image)
    return render(request,'base.html',{"about":data,"home":home, "grouped_photos":group,"popup": popup,"app":app,'ourstory': ourstory})

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

def book_service(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        contact = request.POST['contact']
        service_title = request.POST['service_title']
        booking.objects.create(name=name, email=email, contact=contact, service_title=service_title,address=address)

        # ✅ Render a confirmation popup-style page
        return render(request, 'booking_success.html')
    return redirect('/')

def gallery(request):
    gallery_items = Gallery.objects.all()
    home = hero.objects.all().first()

    return render(request, 'gallery.html', {'gallery_items': gallery_items,"home":home})

# def story(request):
    # ourstory = Ourstory.objects.all()
    # return render(request, 'base.html', {'ourstory': ourstory})
# 
# 
# 