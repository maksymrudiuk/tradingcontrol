from django.contrib import admin
from .models import Company, ContractorCompany

# Register your models here.


class ContractorCompanyInline(admin.TabularInline):
    model = ContractorCompany


class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        ContractorCompanyInline
    ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(ContractorCompany)
