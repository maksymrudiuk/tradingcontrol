from django.contrib import admin
from .models import Company, ContractorCompany
from user.admin import UsersInline

# Register your models here.


class ContractorCompanyInline(admin.TabularInline):
    model = ContractorCompany
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        ContractorCompanyInline
    ]


class ContatctorCompanyAdmin(admin.ModelAdmin):
    inlines = [
        UsersInline
    ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(ContractorCompany, ContatctorCompanyAdmin)
