import logging
from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from formtools.wizard.views import SessionWizardView
from .forms import SignUpForm, Business_type, ComanyForm, WorkingHoursForm, CompanyContactForm
from .models import Rezervace_zivnosti, Company, Zivnosti

Logr = logging.getLogger(__name__)

FORMS = [("basic_company", SignUpForm),
         ("business_type", Business_type),
         ("company", ComanyForm),
         ("adress", CompanyContactForm),
         ("working_hours", WorkingHoursForm)]

TEMPLATES = {"basic_company": "notes/step_one.html",
             "business_type": "notes/business_type.html",
             "company": "notes/step_one.html",
             "adress": "notes/step_one.html",
             "working_hours": "notes/working_hours.html",
             }

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
        # save records into company's object:
        typ_zivnosti = form_data[1]['typ_zivnosti']
        jmeno_zivnosti = form_data[1]['jmeno_zivnosti']
        zivnost = Zivnosti.objects.get(jmeno_zivnosti=jmeno_zivnosti, typ_zivnosti=typ_zivnosti)
        # company's name
        company = Company.objects.create(jmeno_firmy=form_data[2]['jmeno_firmy'], \
        login=user, zivnost=zivnost)
        company.save()

        # company's adress
        company_adress = form_dict['adress']
        company_adress = form_data[2]['jmeno_firmy']
        company_adress.save()

        # sluzby daneho podniku a jeho zamestnanci
        ## Prvni bude blok sluzeb a ve druhe casti bude blok se zamestnanci
        ### Sluzba ma jmeno, cenu a cas
        #### na radce bude: sluzba | cena | cas
        #### -> zkusim dat jeden radek a pridavat dalsi pomoci jquery
        ### Zamestnanec ma jmeno a je mu prirazena sluzba // zjednodusene
        #### na radce bude jmeno zamestnance | 


        #save working hours template into database
        #form_data[3] // odtud budu brat data pro hodiny

        #opravit nasledujici chyby:
            ##predvyplnim hodnoty po-patek od 9-16 pomoci javascriptu
            ## ['ManagementForm data is missing or has been tampered.'] opravit
            ## druhy krok - nefunguje cascade switch

        return render(self.request, 'notes/done.html', {
            'form_data': form_data,
        })
