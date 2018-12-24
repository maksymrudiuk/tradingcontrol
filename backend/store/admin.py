from django.contrib import admin
from .models import Store, GoodsInStore

# Register your models here.


class GoodsInStoreAdmin(admin.ModelAdmin):
    autocomplete_fields = ['store', 'goods']


class GoodsInStoreInline(admin.TabularInline):
    model = GoodsInStore
    extra = 0


class StoreAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [
        GoodsInStoreInline,
    ]


admin.site.register(Store, StoreAdmin)
admin.site.register(GoodsInStore, GoodsInStoreAdmin)
