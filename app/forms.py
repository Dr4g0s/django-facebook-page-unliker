from django import forms
from .models import FacebookPage


class UnlikePagesForm(forms.Form):
    pages = forms.ModelMultipleChoiceField(queryset=FacebookPage.objects.none())

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pages'].queryset = FacebookPage.objects.filter(account__user=user)
