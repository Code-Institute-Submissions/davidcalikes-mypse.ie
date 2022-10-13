from django import forms
from allauth.account.forms import SignupForm


TYPE_CHOICES = (
                    ("pupil", "pupil"),
                    ("parent", "parent"),
                    ("teacher", "teacher"),
                    ("school", "school"),
                    )


class CoreSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CoreSignupForm, self).__init__(*args, **kwargs)
        self.fields['role'] = forms.ChoiceField(choices=TYPE_CHOICES,
                                                label='role')
