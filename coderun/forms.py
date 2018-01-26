from django import forms
from .models import model1


class addData(forms.ModelForm):
    class Meta:
        model = model1
        fields = '__all__'
