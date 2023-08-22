from django import forms
from django.forms import NumberInput
from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField

from core.enums import EmployeeType, PersonalTitle, Gender, MaritalStatus
from .models import Employee


class EmployeeForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=EmployeeType.choices)
    personal_title = forms.ChoiceField(choices=PersonalTitle.choices, required=False)
    date_of_birth = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=Gender.choices, initial=None, required=False)
    nationality = CountryField()
    disability = forms.BooleanField(required=False, initial=False)
    marital_status = forms.ChoiceField(choices=MaritalStatus.choices)
    residential_country = CountryField()
    residential_address = forms.CharField()
    residential_city = forms.CharField()
    residential_postal_code = forms.CharField(required=False)
    residential_phone = PhoneNumberField(required=False)
    personal_email = forms.EmailField()
    direct_manager = forms.ModelChoiceField(queryset=Employee.objects.all(),
                                      label='Direct Manager')

    class Meta:
        model = Employee
        exclude = ["user", "deleted_at", "state", "active", "employees_managed"]
