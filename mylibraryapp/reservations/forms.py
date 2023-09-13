from django import forms

class createForm(forms.Form):
    date_finish = forms.DateTimeField()
    book = forms.IntegerField()