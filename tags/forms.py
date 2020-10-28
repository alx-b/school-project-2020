from django import forms


class AddModeratorForm(forms.Form):
    username = forms.CharField(label="user to add", max_length=100)
