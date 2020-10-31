from django import forms


class TagSelectForm(forms.Form):
    names = forms.MultipleChoiceField(label="Select Tags")

    def __init__(self, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["names"].choices = choices
