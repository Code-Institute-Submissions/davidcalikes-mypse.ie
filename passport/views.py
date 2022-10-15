from django.shortcuts import render, redirect
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
    User with role of 'school' (admin) can add an enrolled pupil to database.
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


class EnrolledPupilList(LoginRequiredMixin, generic.ListView):
    """
    Displays page that lists pupil records created by logged in user
    """
    model = EnrolledPupil
    template_name = 'enrolled_pupil_list.html'
    context_object_name = 'enrolled_pupil_list'

    def get_queryset(self):
        return EnrolledPupil.objects.filter(
            created_by=self.request.user
        )


def LoginSuccess(request):
    """
    Redirects users based on user role
    """
    if request.user.role == "school":
        return redirect('enrolled_pupil_list')
    else:
        return redirect('home')
