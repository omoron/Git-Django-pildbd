from django import forms

class FormContacts(forms.Form):
    subject = forms.CharField()
    email = forms.CharField()
    message = forms.CharField()
