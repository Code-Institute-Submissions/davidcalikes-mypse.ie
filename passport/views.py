from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import EnrolledPupil, Passport
from .forms import EnrolledPupilForm, PassportForm
from django.urls import reverse_lazy
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


class EnrolledPupilRecord(LoginRequiredMixin, View):
    """
    Displays pupil record selected by authenticated user
    """
    def get(self, request, pupil_id, *args, **kwargs):
        """
        Gets selected pupil record
        """
        queryset = EnrolledPupil.objects.all()
        record = get_object_or_404(queryset, pupil_id=pupil_id)

        return render(
            request,
            'enrolled_pupil_record.html',
            {
                "record": record,
            },
        )


class UpdatePupilRecord(LoginRequiredMixin, generic.edit.UpdateView):
    """
    User with role of School Admin can update enrolled existing pupil record
    """
    model = EnrolledPupil
    form_class = EnrolledPupilForm
    template_name = 'enrolled_pupil_form.html'
    success_url = reverse_lazy('enrolled_pupil_list')


class DeletePupilRecord(LoginRequiredMixin, generic.DeleteView):
    """
    User with role of School Admin can delete existing pupil record
    """
    model = EnrolledPupil
    success_url = reverse_lazy('enrolled_pupil_list')

    def delete(self, request, *args, **kwargs):
        return super(DeletePupilRecord, self).delete(request, *args, **kwargs)


class AddPassport(LoginRequiredMixin, generic.CreateView):
    """
    User with role of parent and a valid pupil ID number can create a passport
    """
    model = Passport
    form_class = PassportForm
    template_name = 'passport_form.html'
    success_url = '/'

    def form_valid(self, form):
        """
        Auto applies foreign key and auto generated settings.
        """
        form.instance.created_by = self.request.user
        return super(AddPassport, self).form_valid(form)


class PassportList(LoginRequiredMixin, generic.ListView):
    """
    Displays page that lists any passports created by logged in user (parent)
    """
    model = Passport
    template_name = 'passport_list.html'
    context_object_name = 'passport_list'

    def get_queryset(self):
        return Passport.objects.filter(
            created_by=self.request.user
        )


class PassportDetail(LoginRequiredMixin, View):
    """
    Displays pupil passport selected by authenticated and authorised user
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Gets selected pupil record
        """
        queryset = Passport.objects.all()
        passport = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'passport_detail.html',
            {
                "passport": passport,
            },
        )


def LoginSuccess(request):
    """
    Redirects users based on user role
    """
    if request.user.role == "school":
        return redirect('enrolled_pupil_list')
    elif request.user.role == "parent":
        return redirect('passport_list')
    else:
        return redirect('home')
