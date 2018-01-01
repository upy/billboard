from django import forms

from . import models


class RepresentativeForm(forms.ModelForm):
    class Meta:
        model = models.Representative
        fields = ['username', 'first_name', 'last_name', 'email', 'phone',
                  'is_active']
