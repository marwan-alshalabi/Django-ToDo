from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display=['id','name','date']

admin.site.register(ToDo,ToDoAdmin)