from django import forms
from .models import Participation

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ['fcs', 'institution_name', 'phone', 'email']
        labels = {
            'fcs': 'ФИО',
            'institution_name': 'Название учреждения',
            'phone': 'Телефон',
            'email': 'Email'
        }
        widgets = {
            'fcs': forms.TextInput(attrs={'class': 'form-control'}),
            'institution_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }