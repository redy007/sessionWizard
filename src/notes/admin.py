from django.contrib import admin

# Register your models here.
from .models import Entry, Rezervace_typy_zivnosti, Rezervace_zivnosti

admin.site.register(Entry)
admin.site.register(Rezervace_zivnosti)
admin.site.register(Rezervace_typy_zivnosti)
