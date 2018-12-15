from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Zivnosti, Contact


#session wizard - first step
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class Business_type(forms.ModelForm):
    #https://diskuse.jakpsatweb.cz/?action=vthread&forum=8&topic=166005
    #typ_zivnosti = forms.ChoiceField(label='Obor', required=True)
    #jmeno_zivnosti = forms.ChoiceField(label='Jmeno sluzby', required=True)

    class Meta:
        model = Zivnosti
        fields = ('typ_zivnosti', 'jmeno_zivnosti', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['jmeno_zivnosti'].queryset = Rezervace_zivnosti.objects.none()

# jmeno podniku -> navazat z toho co uz mam
# optional adresa
# optional webove stranky
# preddefinovana oteviraci doba podniku
# sluzby // najit zpusob jak pridavat jednen radek sluzby po druhe
# zamestnanci // najit zpusob jak pridavat jednen radek zamestnance po druhem

# vytvorim master objekt, ktery bude mit referenci na vsechny podniky pod nim

class ComanyForm(forms.ModelForm):
    jmeno_firmy = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Zivnosti
        fields = ('jmeno_firmy', )

class CompanyContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('street', 'city', 'phone', 'url')

class WorkingHoursForm(forms.Form):
    nedele_od = forms.DateTimeField(required=False)
    nedele_do = forms.DateTimeField(required=False)
    pondeli_od = forms.DateTimeField(required=False)
    pondeli_do = forms.DateTimeField(required=False)
    utery_od = forms.DateTimeField(required=False)
    utery_do = forms.DateTimeField(required=False)
    streda_od = forms.DateTimeField(required=False)
    streda_do = forms.DateTimeField(required=False)
    ctvrtek_od = forms.DateTimeField(required=False)
    ctvrtek_do = forms.DateTimeField(required=False)
    patek_od = forms.DateTimeField(required=False)
    patek_do = forms.DateTimeField(required=False)
    sobota_od = forms.DateTimeField(required=False)
    sobota_do = forms.DateTimeField(required=False)
