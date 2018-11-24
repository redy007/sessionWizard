from django.contrib import admin
from django.urls import path
from notes.views import entry_view, ContactWizard, FORMS, load_business_names
#from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entries/', entry_view),
    path('contact/', ContactWizard.as_view(FORMS)),
    path('ajax/load-business/', load_business_names, name='ajax_load_business'),   
]
