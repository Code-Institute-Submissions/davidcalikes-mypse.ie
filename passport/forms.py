from django import forms
from .models import EnrolledPupil, Passport
from allauth.account.forms import SignupForm
from django_summernote.widgets import SummernoteWidget

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
                                                label='Role')


class EnrolledPupilForm(forms.ModelForm):
    """
    Form for adding an enrolled pupil to database
    """
    class Meta:
        """
        Form has all required fields from EnrolledPupil model
        """
        model = EnrolledPupil
        fields = ('pupil_full_name', 'pupil_id', 'school_name',
                  'school_roll_number', 'school_email', )


class PassportForm(forms.ModelForm):
    """
    Form for creating a pupil passport
    """
    class Meta:
        """
        Form has all required fields from Passport model
        """
        model = Passport
        fields = ('pupil_id',
                  'teacher_id',
                  'my_full_name',
                  'my_passport_image',
                  'my_emergency_contact_name',
                  'my_emergency_contact_number',
                  'my_date_of_birth', 'my_biography',
                  'my_family', 'my_family_image', 'my_likes',
                  'my_likes_image', 'my_dislikes',
                  'my_strengths', 'my_difficulties',
                  'my_supports', 'my_supports_image',
                  'my_communication_skills', 'my_communication_skills_image',
                  'my_calming_measures', 'my_other_info',
                  )

        widgets = {
            'my_biography': SummernoteWidget(),
            'my_family': SummernoteWidget(),
            'my_likes': SummernoteWidget(),
            'my_dislikes': SummernoteWidget(),
            'my_strengths': SummernoteWidget(),
            'my_difficulties': SummernoteWidget(),
            'my_supports': SummernoteWidget(),
            'my_calming_measures': SummernoteWidget(),
            'my_communication_skills': SummernoteWidget(),
            'my_other_info': SummernoteWidget(),
        }
