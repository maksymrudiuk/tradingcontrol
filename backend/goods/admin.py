from django.contrib import admin
from .models import Goods

# Register your models here.


class GoodsAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Goods, GoodsAdmin)
