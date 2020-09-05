
from .models import AlbunsPost
from django.forms import ModelForm

class AlbunsForm(ModelForm):
    class Meta:
        model = AlbunsPost
        fields = ['titulo','descricao','arquivo']
        labels = {'observacao':'Titulo post'}
