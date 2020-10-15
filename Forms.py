from .models import *
from django.forms import ModelForm
from django import forms


class StartUpForm(ModelForm):
    class Meta:
        model = StartUp
        fields = "__all__"

        widgets = {
            "Name": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Name'}),
            "Field": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Field'}),
            "Email": forms.EmailInput(attrs={'class': 'textbox', 'placeholder': 'Email'}),
            "Description": forms.Textarea(attrs={'class': 'textbox', 'placeholder': 'Description'})
        }


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Name'}),
            "Field": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Field'}),
            "Email": forms.EmailInput(attrs={'class': 'textbox', 'placeholder': 'Email'}),
            "Query": forms.Textarea(attrs={'class': 'textbox', 'placeholder': 'Enter your query...'})
        }


class InvestorForm(ModelForm):
    class Meta:
        model = Investor
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Name'}),
            "Field": forms.TextInput(attrs={'class': 'textbox', 'placeholder': 'Area of interest'}),
            "Email": forms.EmailInput(attrs={'class': 'textbox', 'placeholder': 'Email'}),

        }
