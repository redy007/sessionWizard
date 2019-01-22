from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from notes.views import ContactWizard, FORMS, load_business_names

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', ContactWizard.as_view(FORMS)),
    path('ajax/load-business/', load_business_names, name='ajax_load_business'), 
    path('', RedirectView.as_view(url='contact/', permanent=True)),  
]
