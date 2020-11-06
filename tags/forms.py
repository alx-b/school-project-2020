from django import forms


class ModeratorForm(forms.Form):
    username = forms.CharField(label="user to add or remove", max_length=100)
