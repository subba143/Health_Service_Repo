from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
class VendorForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    contact = forms.IntegerField()
    item = forms.CharField()


