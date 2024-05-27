from django import  forms
from MovieApp.models import MovieDb
class MovieForm(forms.ModelForm):
    class Meta:
        model    =   MovieDb
        fields  =   '__all__'