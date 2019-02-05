from django.contrib import admin

# Register your models here.
from .models import Business, BusinessCategories, BusinessTypes

# admin.site.register(Entry)
# admin.site.register(Business)
# admin.site.register(BusinessTypes)

class InLineBusinessCategory(admin.TabularInline):
    model = BusinessCategories

class InLineBusinessType(admin.TabularInline):
    model = BusinessTypes

class InLineBusiness(admin.TabularInline):
    model = Business
    extra = 1

""" class BusinessAdmin(admin.ModelAdmin):
    inlines = [InLineBusinessType, InLineBusinessCategory]
    # list_display = ('business_category',)
    # fields = ('business_category')

admin.site.register(Business, BusinessAdmin)
"""

class BusinessCategoryAdmin(admin.ModelAdmin):
    inlines = [InLineBusiness]
    # list_display = ('business_category',)
    # fields = ('business_category')

admin.site.register(BusinessCategories, BusinessCategoryAdmin)

class BusinessTypeAdmin(admin.ModelAdmin):
    inlines = [InLineBusiness]
    # list_display = ('business_category',)
    # fields = ('business_category')

admin.site.register(BusinessTypes, BusinessTypeAdmin)
