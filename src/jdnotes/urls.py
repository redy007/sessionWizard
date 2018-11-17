from django.contrib import admin
from django.urls import path
from notes.forms import SignUpForm , Business_type, ContactForm3
from notes.views import entry_view, ContactWizard, FORMS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entries/', entry_view),
    path('contact/', ContactWizard.as_view(FORMS)),
]
