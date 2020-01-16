from django.contrib import admin

# Register your models here.
from .models import Meme

class MemeAdmin(admin.ModelAdmin):
    fields = ['url', 'name']
    list_display = ['url', 'name']

admin.site.register(Meme, MemeAdmin)