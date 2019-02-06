from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from formtools.wizard.views import SessionWizardView
import uuid 
from .forms import SignUpForm, Business_type, CompanyForm, CompanyContactForm
from .models import BusinessTypes, BusinessCategories, Company, Business, Contact

FORMS = [("basic_company", SignUpForm),
         ("business_type", Business_type),
         ("company", CompanyForm),
         ("adress", CompanyContactForm),
         ]

TEMPLATES = {"basic_company": "notes/login.html",
             "business_type": "notes/business_type.html",
             "company": "notes/company_name.html",
             "adress": "notes/company_details.html",
             }

initial = {}

def load_business_names(request):
    zivnosti_id = request.GET.get('business')
    zivnost = BusinessTypes.objects.filter(business_category=zivnosti_id) \
    .order_by('business_name')
    return render(request, 'notes/notes_business_dropdown_list_options.html', {'zivnosti': zivnost})

class ContactWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        if step == 'adress':
            company_name = self.get_cleaned_data_for_step('company')
            initial.update({'company_name': company_name['company_name']})
        return initial

    def done(self, form_list, form_dict, **kwargs):
        user = form_dict['basic_company'].save()

        form_data = [form.cleaned_data for form in form_list]
        # save records into company's object:
        business_category = form_data[1]['business_category']
        business_category_obj = BusinessCategories.objects.get(business_category=business_category)
        business_name = form_data[1]['business_name']
        business_name_obj = BusinessTypes.objects.get(business_name=business_name)
        
        # business_name = form_data[1]['business_name']
        business = Business.objects.get(business_name=business_name_obj, business_category=business_category_obj)
        # company's name
        
        company_uuid = uuid.uuid4()
        company = Company.objects.create(company_name=form_data[2]['company_name'], \
        login=user, business=business, company_uuid=company_uuid)
        company.save()

        # company's adress
        company = Contact.objects.create(company=company, \
        street=form_data[3]['street'], city=form_data[3]['city'], \
        phone=form_data[3]['phone'], url=form_data[3]['url'])



        return render(self.request, 'notes/done.html', {
            'form_data': form_data,
            'uuid': company_uuid,
        })
