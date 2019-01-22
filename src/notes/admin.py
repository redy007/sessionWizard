from django.contrib import admin

# Register your models here.
from .models import Entry, Business, BusinessCategories, BusinessTypes

admin.site.register(Entry)
admin.site.register(Business)
admin.site.register(BusinessTypes)

class InLineBusinessType(admin.TabularInline):
    model = BusinessTypes

class BusinessCatergoryAdmin(admin.ModelAdmin):
    inlines = [InLineBusinessType]
    list_display = ('business_category',)
    # fields = ('business_category')

admin.site.register(BusinessCategories, BusinessCatergoryAdmin)
