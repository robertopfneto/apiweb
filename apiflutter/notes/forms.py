from django import forms
from .models import Person, Profession

from django import forms
from .models import Person, Profession

class PersonForm(forms.ModelForm):
    
    fk_profession = forms.ModelChoiceField(queryset=Profession.objects.all())

    class Meta:
        model = Person
        fields = ['name', 'age', 'cpf', 'data_nascimento', 'fk_profession']

class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ['name']        