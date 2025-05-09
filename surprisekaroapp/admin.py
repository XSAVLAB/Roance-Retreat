from django.contrib import admin
from .models import about, service, data, photo, booking, hero
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display=["name","email","booking_date", "service_title","contact"]
    
class DataAdmin(admin.ModelAdmin):
    list_display=["name","email","message", "subject"]

    

admin.site.register(about)
admin.site.register(service)
admin.site.register(data,DataAdmin)
admin.site.register(photo)
admin.site.register(booking,BookingAdmin)
admin.site.register(hero)

admin.site.site_title="Romance Retreat"
admin.site.site_header="Romance Retreat"