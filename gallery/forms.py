from django.forms import ModelForm
from .models import Image

class  ImageCreateForm(ModelForm):

    class Meta:
        model = Image
        exclude = ['contributor', ]
