from django import forms
from .models import *
#from django.forms import Textarea, TextInput


class SubscriberForm(forms.ModelForm):

    # Instances Meta(metaclass) are classes.In this case, Meta construct SubscriberForm
    # And we redefine fields i.e. model, exclude  in class Meta
    class Meta:
        model = Subscriber
        exclude = [""]
        #fields = ("email", "name")
        #widgets = {
         #   'email': TextInput(attrs={'style': 'padding-left:3px;', 'placeholder': 'Email'}),
          #  'name': TextInput(attrs={'style': 'padding-left:3px;', 'placeholder': 'Name'}),
        #}
