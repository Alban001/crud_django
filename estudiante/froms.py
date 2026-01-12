from django import forms
from estudiante.models import Estudiante

class EstudianteForms(forms.ModelForm):

    class Meta:
        
        model = Estudiante
        fields = ["nombre","edad","email","ciudad"]