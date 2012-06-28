from django.forms.models import ModelForm
from django.forms import CharField
from django.forms.widgets import HiddenInput, TextInput
from models import Button
from picasabuttonizer.models import HybridButton, TrayexecButton, OpenButton

__author__ = 'fatrix'

class ButtonForm(ModelForm):
    guid = CharField(widget=HiddenInput(), required=False)
    id = CharField(widget=HiddenInput(), required=False)
    class Meta:
        model = Button
        exclude = ('user')

class HybridButtonForm(ModelForm):
    class Meta:
        model = HybridButton

class TrayexecButtonForm(ModelForm):
    class Meta:
        model = TrayexecButton

class OpenButtonForm(ModelForm):
    class Meta:
        model = OpenButton

