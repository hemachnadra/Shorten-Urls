from django import forms


class Url(forms.Form):
    url=forms.CharField(label='URL to be shorting...')