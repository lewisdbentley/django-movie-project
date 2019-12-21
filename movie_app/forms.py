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

class MovieCreateForm(forms.Form):
    title = forms.CharField(max_length=30)
    owner = forms.CharField(max_length=30)
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write a description of the movie!'
        )
    source = forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(MovieCreateForm, self).clean()
        title = cleaned_data.get('title')
        owner = cleaned_data.get('owner')
        description = cleaned_data.get('description')
        if not title and not owner and not description:
            raise forms.ValidationError('You have to write something!')