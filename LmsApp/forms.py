from django import forms
from LmsApp.models import Library
class LibraryForm(forms.ModelForm):
    class Meta:
        model =Library
        fields='__all__'
