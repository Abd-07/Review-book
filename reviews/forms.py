from django import forms

from reviews.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['name','email','rating','review']
        widgets={'rating':forms.NumberInput()}
        attrs={'min':1,'max':10}