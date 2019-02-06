from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Business, Contact, BusinessTypes, Company


#session wizard - first step
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class Business_type(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('business_category', 'business_name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['business_name'].queryset = BusinessTypes.objects.none()
        # https://stackoverflow.com/questions/48041375/django-select-a-valid-choice-that-choice-is-not-one-of-the-available-choices
        # https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html
        
        if 'business_type-business_category' in self.data:
            try:
                business_category_id = int(self.data.get('business_type-business_category'))
                self.fields['business_name'].queryset = BusinessTypes.objects.filter(business_category=business_category_id).order_by('business_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset

class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Company
        fields = ('company_name', )

class CompanyContactForm(forms.ModelForm):
    company_name = forms.CharField(disabled=True)

    class Meta:
        model = Contact
        fields = ('company_name','street', 'city', 'phone', 'url')

