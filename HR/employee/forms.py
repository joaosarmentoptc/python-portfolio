import phonenumber_field.widgets
from django import forms
from django.contrib.auth.models import User
from django.forms import NumberInput
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.formfields import PhoneNumberField

from core.enums import EmployeeType, Gender, MaritalStatus
from .models import Employee


class EmployeeForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=EmployeeType.choices, required=True)
    date_of_birth = forms.DateField(widget=forms.widgets.TextInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=Gender.choices, initial=None, required=False)
    nationality = CountryField()
    disability = forms.BooleanField(required=False, initial=False, widget=forms.widgets.CheckboxInput(
        attrs={
            'type': 'checkbox'
        }
    ))
    marital_status = forms.ChoiceField(choices=MaritalStatus.choices)
    residential_country = CountryField(blank_label="(Select Country)")
    residential_address = forms.CharField(widget=forms.widgets.TextInput(attrs={
        'class': 'input', 'type': 'text', 'placeholder': 'Residential Address'
    }))
    residential_city = forms.CharField(widget=forms.widgets.TextInput(attrs={
        'class': 'input', 'type': 'text', 'placeholder': 'Residential City'
    }))
    residential_postal_code = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={
        'class': 'input', 'type': 'text', 'placeholder': 'Postal Code'
    }))
    residential_phone = PhoneNumberField(required=False, widget=phonenumber_field.widgets.PhoneNumberPrefixWidget(
        country_choices=residential_country.countries,
        attrs={
            'class': 'input', 'type': 'tel', 'placeholder': 'Phone Number'
        }))
    personal_email = forms.EmailField(widget=forms.widgets.EmailInput(
        attrs={
            'class': 'input', 'type': 'email', 'placeholder': 'Personal Email'
        }
    ))
    direct_manager = forms.ModelChoiceField(queryset=Employee.objects.all(),
                                            label='Direct Manager')

    class Meta:
        model = Employee
        exclude = ["user", "deleted_at", "state", "active", "employees_managed"]
        widgets = {"country": CountrySelectWidget()}


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.widgets.TextInput(attrs={
        'class': 'input', 'type': 'text', 'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.widgets.TextInput(attrs={
        'class': 'input', 'type': 'text', 'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.widgets.EmailInput(
        attrs={
            'class': 'input', 'type': 'email', 'placeholder': 'Work Email'
        }
    ), disabled=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
