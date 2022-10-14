from django.shortcuts import render
from django.views import generic
from .models import EnrolledPupil
from .forms import EnrolledPupilForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(generic.TemplateView):
    """
    Displays instructional video and links on landing page
    """
    template_name = 'index.html'


class AddEnrolledPupil(LoginRequiredMixin, generic.CreateView):
    """
    User with role of School Admin can add an enrolled pupil to database.
    """
    model = EnrolledPupil
    form_class = EnrolledPupilForm
    template_name = 'enrolled_pupil_form.html'
    success_url = '/'

    def form_valid(self, form):
        """
        Auto applies foreign key and auto generated settings.
        """
        form.instance.created_by = self.request.user
        return super(AddEnrolledPupil, self).form_valid(form)
