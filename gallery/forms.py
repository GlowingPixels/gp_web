from django.forms import ModelForm
from .models import Gallery

class  ImageCreateForm(ModelForm):

    class Meta:
        model = Gallery
        exclude = ['contributor', ]
