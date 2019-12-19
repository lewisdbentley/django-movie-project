from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class MovieVoteForm(forms.Form):
    vote = forms.IntegerField(help_text="Enter a number between 0 and 5.")

    def clean_vote(self):
        data = self.cleaned_data['vote']

        # Check if number is not less than 0.
        if data < 0:
            raise ValidationError(_('Invalid number - less than zero.'))

        # Check if number is not greater than 5.
        if data > 5:
            raise ValidationError(_('Invalid number - greater than five.'))

        return data