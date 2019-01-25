from django.contrib import admin
from .models import Region, City, Route, AgentStore

# Register your models here.


class AgentStoreAdmin(admin.ModelAdmin):
    autocomplete_fields = ['agent_store']


class AgentStoreInline(admin.TabularInline):
    model = AgentStore
    extra = 0


class RouteAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [
        AgentStoreInline,
    ]


admin.site.register(City)
admin.site.register(Region)
admin.site.register(AgentStore, AgentStoreAdmin)
admin.site.register(Route, RouteAdmin)
