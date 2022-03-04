from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    review = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(min_value=1,max_value=10)