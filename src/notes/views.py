from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from formtools.wizard.views import SessionWizardView
from .forms import SignUpForm, Business_type, CompanyForm, WorkingHoursForm, CompanyContactForm
from .models import BusinessTypes, Company, Business, OpenHours

FORMS = [("basic_company", SignUpForm),
         ("business_type", Business_type),
         ("company", CompanyForm),
         ("adress", CompanyContactForm),
         #("working_hours", WorkingHoursForm),
         ]

TEMPLATES = {"basic_company": "notes/login.html",
             "business_type": "notes/business_type.html",
             "company": "notes/company_name.html",
             "adress": "notes/company_details.html",
             #"working_hours": "notes/working_hours.html",
             }

def load_business_names(request):
    zivnosti_id = request.GET.get('business')
    zivnost = BusinessTypes.objects.filter(business_category=zivnosti_id) \
    .order_by('business_name')
    return render(request, 'notes/notes_business_dropdown_list_options.html', {'zivnosti': zivnost})

class ContactWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_initial(self, step):
        if step == 'working_hours':
            return self.initial_dict.get(step, {'monday_from': '9:00', 'monday_to': '17:00'})
        return self.initial_dict.get(step, {})

    def done(self, form_list, form_dict, **kwargs):
        user = form_dict['basic_company'].save()

        form_data = [form.cleaned_data for form in form_list]
        # save records into company's object:
        # form_data[1]: {'business_category': <Rezervace_typy_zivnosti: sluzby>, 'business_name': <Rezervace_zivnosti: Damske kadernictvi>}
        print("form_data[1]: " + str(form_data[1]))
        business_category = form_data[1]['Rezervace_typy_zivnosti']
        business_name = form_data[1]['business_name']
        zivnost = Zivnosti.objects.get(business_name=business_name, business_category=business_category)
        # company's name
        company = Company.objects.create(company_name=form_data[2]['company_name'], \
        login=user, zivnost=zivnost)
        company.save()

        # company's adress
        company_adress = form_dict[2]['street']
        company_adress = form_data[2]['city']
        company_adress = form_data[2]['phone']
        company_adress = form_data[2]['url']
        company_adress.save()

        hours_dict = {}
        hours_dict['company'] = company
        hours_dict['open_from'] = form_data[3]['sunday_from']
        hours_dict['open_to'] = form_data[3]['sunday_to']
        if (hours_dict['open_from'] and hours_dict['open_to']):
            hours_dict['day'] = 0
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'open_from': hours_dict['open_from'], 'open_to': hours_dict['open_to'], 'company': hours_dict['company'], 'pracuje': 'T'})  
        else:
            hours_dict['day'] = 0
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'pracuje': 'F'})  
        hours_dict['open_from'] = form_data[3]['monday_from']
        hours_dict['open_to'] = form_data[3]['monday_to']
        if (hours_dict['open_from'] and hours_dict['open_to']):
            hours_dict['day'] = 1
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'open_from': hours_dict['open_from'], 'open_to': hours_dict['open_to'], 'company': hours_dict['company'], 'pracuje': 'T'})  
        else:
            hours_dict['day'] = 1
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'pracuje': 'F'})  
        hours_dict['open_from'] = form_data[3]['tuesday_from']
        hours_dict['open_to'] = form_data[3]['tuesday_to']
        if (hours_dict['open_from'] and hours_dict['open_to']):
            hours_dict['day'] = 2
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'open_from': hours_dict['open_from'], 'open_to': hours_dict['open_to'], 'company': hours_dict['company'], 'pracuje': 'T'})  
        else:
            hours_dict['day'] = 2
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'pracuje': 'F'})  
        hours_dict['open_from'] = form_data[3]['wednesday_from']
        hours_dict['open_to'] = form_data[3]['wednesday_to']
        if (hours_dict['open_from'] and hours_dict['open_to']):
            hours_dict['day'] = 3
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'open_from': hours_dict['open_from'], 'open_to': hours_dict['open_to'], 'company': hours_dict['company'], 'pracuje': 'T'})  
        else:
            hours_dict['day'] = 3
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'pracuje': 'F'})  
        hours_dict['open_from'] = form_data[3]['thursday_from']
        hours_dict['open_to'] = form_data[3]['thursday_to']
        if (hours_dict['open_from'] and hours_dict['open_to']):
            hours_dict['day'] = 4
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'open_from': hours_dict['open_from'], 'open_to': hours_dict['open_to'], 'company': hours_dict['company'], 'pracuje': 'T'})  
        else:
            hours_dict['day'] = 4
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'pracuje': 'F'})  
        hours_dict['open_from'] = form_data[3]['friday_from']
        hours_dict['open_to'] = form_data[3]['friday_to']
        if (hours_dict['open_from'] and hours_dict['open_to']):
            hours_dict['day'] = 5
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'open_from': hours_dict['open_from'], 'open_to': hours_dict['open_to'], 'company': hours_dict['company'], 'pracuje': 'T'})  
        else:
            hours_dict['day'] = 5
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'pracuje': 'F'})  
        hours_dict['open_from'] = form_data[3]['saturday_from']
        hours_dict['open_to'] = form_data[3]['saturday_to']
        if (hours_dict['open_from'] and hours_dict['open_to']):
            hours_dict['day'] = 6
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'open_from': hours_dict['open_from'], 'open_to': hours_dict['open_to'], 'company': hours_dict['company'], 'pracuje': 'T'})  
        else:
            hours_dict['day'] = 6
            obj, created = OpenHours.objects.update_or_create(company=hours_dict['company'], day=hours_dict['day'], defaults={'day': hours_dict['day'], 'pracuje': 'F'})  
        

        # sluzby daneho podniku a jeho zamestnanci
        ## Prvni bude blok sluzeb a ve druhe casti bude blok se zamestnanci
        ### Sluzba ma jmeno, cenu a cas
        #### na radce bude: sluzba | cena | cas
        #### -> zkusim dat jeday radek a pridavat dalsi pomoci jquery
        ### Zamestnanec ma jmeno a je mu prirazena sluzba // zjednodusene
        #### na radce bude jmeno zamestnance | 


        #save working hours template into database
        #form_data[3] // odtud budu brat data pro hodiny

        #opravit nasledujici chyby:
            ##predvyplnim hodnoty po-patek od 9-16 pomoci javascriptu
            ## ['ManagementForm data is missing or has been tampered.'] opravit
            ## druhy krok - nefunguje cascade switch

        return render(self.request, 'notes/done.html', {
            'form_data': form_data[1],
        })
