from django import forms
from .models import Knjiga
class KnjigaForm(forms.ModelForm):
    class Meta:
        model=Knjiga
        fields=['naslov','autor','zanr','godina','opis','kolicina']
        widgets={
            'opis':forms.Textarea(attrs={'rows':4}),
        }