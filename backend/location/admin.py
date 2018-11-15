from django.contrib import admin
from .models import Area, City, Route

# Register your models here.

admin.site.register(City)
admin.site.register(Area)
admin.site.register(Route)
