from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import EnrolledPupil, Passport
from .forms import EnrolledPupilForm, PassportForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(generic.TemplateView):
    """
    Displays instructional video and links on landing page
    """
    template_name = 'index.html'


class AddEnrolledPupil(LoginRequiredMixin, SuccessMessageMixin,
                       generic.CreateView):
    """
    User with role of 'school' (admin) can add an enrolled pupil to database.
    """
    model = EnrolledPupil
    form_class = EnrolledPupilForm
    template_name = 'enrolled_pupil_form.html'
    success_url = reverse_lazy('enrolled_pupil_list')
    success_message = "Pupil record added successfully!"

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


class UpdatePupilRecord(LoginRequiredMixin, SuccessMessageMixin, generic.edit.UpdateView):
    """
    User with role of School Admin can update enrolled existing pupil record
    """
    model = EnrolledPupil
    form_class = EnrolledPupilForm
    template_name = 'enrolled_pupil_form.html'
    success_url = reverse_lazy('enrolled_pupil_list')
    success_message = "Pupil record updated successfully!"


class DeletePupilRecord(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    """
    User with role of School Admin can delete existing pupil record
    """
    model = EnrolledPupil
    success_url = reverse_lazy('enrolled_pupil_list')
    success_message = "Pupil record deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePupilRecord, self).delete(request, *args, **kwargs)


class ValidatePupilId(generic.ListView, SuccessMessageMixin):
    """
    Ensures Pupil is enrolled in system before a passport can be created
    """
    template_name = 'validate_pupil_id.html'
    model = EnrolledPupil
    success_message = "No matching record found!"

    def get_queryset(self):
        query = self.request.GET.get('pupil_id')
        if query:
            object_list = self.model.objects.filter(pupil_id__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


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

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


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


class UpdatePassport(LoginRequiredMixin, generic.edit.UpdateView):
    """
    Authenticated user with authorisation can update passport information
    """
    model = Passport
    form_class = PassportForm
    template_name = 'passport_form.html'
    success_url = reverse_lazy('passport_list')


class DeletePassport(LoginRequiredMixin, generic.DeleteView):
    """
    Authenticated user with authorisation can delete a passport
    """
    model = Passport
    success_url = reverse_lazy('passport_list')

    def delete(self, request, *args, **kwargs):
        return super(DeletePassport, self).delete(request, *args, **kwargs)


class TeacherPassportList(generic.ListView):
    """
    Displays list of pupil passports when corresponding teacher id is typed
    """
    model = Passport
    template_name = 'teacher_passport_list.html'

    def get_queryset(self):
        query = self.request.GET.get('teacher_id')
        if query:
            object_list = self.model.objects.filter(
                teacher_id__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class TeacherValidatePupilId(generic.ListView):
    """
    Ensures Teacher has access to Pupil ID  before a passport can be viewed
    """
    template_name = 'teacher_validate_pupil_id.html'
    model = Passport

    def get_queryset(self):
        print(self.request.GET)
        query = self.request.GET.get('pupil_id')
        if query:
            object_list = self.model.objects.filter(pupil_id__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class TeacherPassportDetail(LoginRequiredMixin, View):
    """
    Displays passport selected by authenticated and authorised teacher
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Gets selected pupil record
        """
        queryset = Passport.objects.all()
        passport = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'teacher_passport_detail.html',
            {
                "passport": passport,
            },
        )


class PupilCheck(LoginRequiredMixin, generic.ListView):
    """
    Displays page that lists pupil records created by logged in user
    """
    model = Passport
    template_name = 'pupil_check.html'
    context_object_name = 'pupil_check'

    def get_queryset(self):
        return Passport.objects.filter(
            created_by=self.request.user
        )


def LoginSuccess(request):
    """
    Redirects users based on user role
    """
    if request.user.role == "school":
        return redirect('enrolled_pupil_list')
    elif request.user.role == "parent":
        return redirect('passport_list')
    elif request.user.role == "teacher":
        return redirect("teacher_passport_list")
    elif request.user.role == "pupil":
        return redirect("pupil_check")
    else:
        return redirect("home")
