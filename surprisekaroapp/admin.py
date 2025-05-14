from django.contrib import admin
from .models import about, service, data, photo, booking, hero, PopupImage, Gallery, Ourstory, Whatsapp
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display=["name","email","booking_date", "service_title","address","contact"]
    
class DataAdmin(admin.ModelAdmin):
    list_display=["name","email","message", "subject"]
    
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'video_url', 'created_at', 'updated_at')
    search_fields = ('title',)

# @admin.register(PopupImage)
# class PopupImageAdmin(admin.ModelAdmin):
    # list_display = ['id', 'is_active', 'updated_at']
    

    

admin.site.register(about)
admin.site.register(service)
admin.site.register(data,DataAdmin)
admin.site.register(photo)
admin.site.register(booking,BookingAdmin)
admin.site.register(hero)
admin.site.register(PopupImage)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Ourstory)
admin.site.register(Whatsapp)


admin.site.site_title="Romance Retreat"
admin.site.site_header="Romance Retreat"