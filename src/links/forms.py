from django import forms


class AddLinkForm(forms.Form):
    url = forms.URLField()





