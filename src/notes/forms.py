from django import forms
from .models import Rezervace_typy_zivnosti, Rezervace_zivnosti
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#session wizard - first step
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    group = forms.CharField(label='Company', min_length=4, max_length=40, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'group', )

class Business_type(forms.ModelForm):
    #https://diskuse.jakpsatweb.cz/?action=vthread&forum=8&topic=166005
    jmeno_zivnosti = forms.CharField(label='Company type', required=True)

    class Meta:
        model = Rezervace_zivnosti
        fields = ('typ_zivnosti', 'jmeno_zivnosti', )

class ContactForm2(forms.Form):
    sender = forms.EmailField()

class ContactForm3(forms.Form):
    message = forms.CharField(widget=forms.Textarea)