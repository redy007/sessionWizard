import logging
from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from formtools.wizard.views import SessionWizardView
from .forms import SignUpForm, Business_type, ComanyForm
from .models import Entry, Rezervace_zivnosti, Firma, Zivnosti

Logr = logging.getLogger(__name__)

FORMS = [("basic_company", SignUpForm),
         ("business_type", Business_type),
         ("company", ComanyForm)]

TEMPLATES = {"basic_company": "notes/step_one.html",
             "business_type": "notes/business_type.html",
             "company": "notes/step_one.html"}

def load_business_names(request):
    zivnosti_id = request.GET.get('business')
    zivnost = Rezervace_zivnosti.objects.filter(typ_zivnosti=zivnosti_id) \
    .order_by('jmeno_zivnosti')
    return render(request, 'notes/notes_business_dropdown_list_options.html', {'zivnosti': zivnost})

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
        user = form_dict['basic_company'].save()
        form_data = [form.cleaned_data for form in form_list]
        typ_zivnosti = form_data[1]['typ_zivnosti']
        jmeno_zivnosti = form_data[1]['jmeno_zivnosti']
        zivnost = Zivnosti.objects.get(jmeno_zivnosti=jmeno_zivnosti, typ_zivnosti=typ_zivnosti)
        firma = Firma.objects.create(jmeno_firmy=form_data[2]['jmeno_firmy'], \
        login=user, zivnost=zivnost)
        firma.save()

        return render(self.request, 'notes/done.html', {
            'form_data': form_data,
        })
