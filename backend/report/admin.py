from django.contrib import admin
from .models import ReportData, ReportItem


class ReportItemInline(admin.TabularInline):
    model = ReportItem
    extra = 0


class ReportDataAdmin(admin.ModelAdmin):

    inlines = [
        ReportItemInline,
    ]


admin.site.register(ReportData, ReportDataAdmin)
admin.site.register(ReportItem)
