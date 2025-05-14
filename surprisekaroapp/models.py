from django.db import models

# Create your models here.
class about(models.Model):
    title= models.CharField(max_length=225)
    description= models.TextField()
    image=models.ImageField(upload_to='about_image/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title
    
class service(models.Model):
    title= models.CharField(max_length=225)
    description= models.TextField()
    price= models.CharField(max_length=100, null=True)
    image=models.ImageField(upload_to='service_images/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title
    
class booking(models.Model):
    name= models.CharField(max_length=225, null=True, blank=True)
    email= models.TextField(null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    days = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=225, null=True)
    contact = models.IntegerField(null=True, blank=True)
    service_title = models.CharField(max_length=225,null=True)
    def __str__(self):
        return self.name
    
class data(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length= 255)
    subject = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
     return self.name
    
class photo(models.Model):
    title= models.CharField(max_length=225)
    image=models.ImageField(upload_to='portfolio/')
    eventype=models.CharField(max_length=225, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title
    
class hero(models.Model):
    image=models.ImageField(upload_to='home/')
    
#class user(models.Model):

class PopupImage(models.Model):
    image = models.ImageField(upload_to='popup/')
    is_active = models.BooleanField(default=True)  # Only show if active
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Popup Image - {self.updated_at.strftime('%Y-%m-%d')}"
    
class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)  # For video URL
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Ourstory(models.Model):
    image =  models.ImageField(upload_to='story/',null=True,blank=True)
    description1 = models.TextField(null=True)
    description2 = models.TextField(null=True)
    
    def __str__(self):
     return f"Our Story Image"
 
class Whatsapp(models.Model):
    name = models.CharField(max_length=100,null=True)
    number = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    