from django.contrib import admin
from myapp.models import Image

# Register your models here.
admin.site.register(Image)
list_display = ['id','photo','date']