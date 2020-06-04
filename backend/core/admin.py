from django.contrib import admin

from .models import Crop


class CropAdmin(admin.ModelAdmin):
    #fields = ['', '']
    # list_filter = ['']
    list_display = ['name','description',]

admin.site.register(Crop, CropAdmin)