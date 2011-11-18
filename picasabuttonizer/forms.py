from django.forms.models import ModelForm
from django.forms import CharField
from django.forms.widgets import HiddenInput, TextInput
from models import Button

__author__ = 'fatrix'

class ButtonForm(ModelForm):
    guid = CharField(widget=HiddenInput(), required=False)
    id = CharField(widget=HiddenInput(), required=False)
    hybrid_uploader_url = CharField(widget=TextInput(attrs={'size':'30'}))
    class Meta:
        model = Button
        exclude = ('user')

    #def clean_hybrid_uploader_url(self):
    #    return self.cleaned_data['hybrid_uploader_url']
