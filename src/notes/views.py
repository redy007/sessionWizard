import logging
from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from formtools.wizard.views import SessionWizardView
from .forms import SignUpForm, Business_type, ContactForm3
from .models import Entry

Logr = logging.getLogger(__name__)

FORMS = [("basic_details", SignUpForm),
         ("business_type", Business_type),
         ("message", ContactForm3)]

TEMPLATES = {"basic_details": "notes/step_one.html",
             "business_type": "notes/business_type.html",
             "message": "notes/step_one.html"}

# Create your views here.
def entry_view(request):
    """ Entry view """
    all_entries = Entry.objects.all()
    context = {
        'object_list': all_entries
    }
    return render(request, "notes/entries.html", context)

class ContactWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    #template_name = 'notes/step_one.html'

    def get_form_initial(self, step):
        return self.initial_dict.get(step, {})

    def done(self, form_list, form_dict, **kwargs):
        Logr.debug(form_dict[0]['subject'])
        Logr.debug(form_dict[0]['sender'])
        Logr.debug(form_dict[0]['message'])
        return render(self.request, 'notes/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
