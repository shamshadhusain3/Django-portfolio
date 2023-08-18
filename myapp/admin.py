from django.contrib import admin
from .models import contact

# Register your models here.
class adminModel(admin.ModelAdmin):
    list_display=['name', 'email', 'address']


admin.site.register(contact,adminModel)