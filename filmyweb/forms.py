from django.forms import ModelForm
from .models import Film, DodatkoweInfo, Ocena

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'opis', 'premiera', 'rok', 'imdb_rating', 'plakat']


class DodatkoweInfoForm(ModelForm):
    class Meta:
        model = DodatkoweInfo
        fields = ['czas_trwania', 'gatunek']

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['gwiazdki', 'recenzja']
