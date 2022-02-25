from django import forms
from .models import Portfolio, Contact


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['p_name', 'p_desc', 'p_image']


class ContactFrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['c_name', 'c_email', 'c_message']