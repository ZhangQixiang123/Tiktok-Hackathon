from django.contrib import admin

# Register your models here.

from .models import Video, Commodity

admin.site.register(Video)
admin.site.register(Commodity)

