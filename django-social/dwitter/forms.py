from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': 'Dweet something...',
                'class': 'text-area is-success is-medium is-fullwidth'
            }
        ),
        label=''
    )

    class Meta:
        model = Dweet
        exclude = ("user", )
