from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Zivnosti, Rezervace_zivnosti


#session wizard - first step
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    group = forms.CharField(label='Company', min_length=4, max_length=40, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'group', )

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

class Business_details_form(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
