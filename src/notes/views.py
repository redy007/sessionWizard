from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from formtools.wizard.views import SessionWizardView
from .forms import SignUpForm, Business_type, CompanyForm, WorkingHoursForm, CompanyContactForm
from .models import BusinessTypes, BusinessCategories, Company, Business

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
        return self.initial_dict.get(step, {})

    def done(self, form_list, form_dict, **kwargs):
        user = form_dict['basic_company'].save()

        form_data = [form.cleaned_data for form in form_list]
        # save records into company's object:
        # form_data[1]: {'business_category': <Rezervace_typy_zivnosti: sluzby>, 'business_name': <Rezervace_zivnosti: Damske kadernictvi>}
        print("form_data[1]: " + str(form_data[1]))
        #print("form_data[1]: " + str(form_data[1]['business_category'])
        business_category = form_data[1]['business_category']
        business_category_obj = BusinessCategories.objects.get(business_category=business_category)
        business_name = form_data[1]['business_name']
        business_name_obj = BusinessTypes.objects.get(business_name=business_name)
        print(business_category_obj)
        print(business_name_obj)
        
        #business_name = form_data[1]['business_name']
        business = Business.objects.get(business_name=business_name_obj, business_category=business_category_obj)
        # company's name
        
        company = Company.objects.create(company_name=form_data[2]['company_name'], \
        login=user, business=business)
        company.save()

        # company's adress
        company_adress = form_dict[2]['street']
        company_adress = form_data[2]['city']
        company_adress = form_data[2]['phone']
        company_adress = form_data[2]['url']
        company_adress.save()



        return render(self.request, 'notes/done.html', {
            'form_data': form_data[1],
        })
