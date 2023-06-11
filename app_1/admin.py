from django.contrib import admin
from .models import place, head_dept, user_data

# Register your models here.
admin.site.register(place)
admin.site.register(head_dept)
admin.site.register(user_data)
