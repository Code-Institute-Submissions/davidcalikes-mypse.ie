from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import EnrolledPupil, Passport
from .forms import EnrolledPupilForm, PassportForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import PageTitleMixin
from django.http import HttpResponse
from django.views.decorators.http import require_GET


class HomePage(PageTitleMixin, generic.TemplateView):
    """
    Displays hero image and cards section with login/about
    links on landing page.
    """
    template_name = 'index.html'
    page_title = "MyPSE.ie - Home"


class AboutPage(PageTitleMixin, generic.TemplateView):
    """
    Displays about page with useful information and
    mock passports to inspire users.
    """
    template_name = 'about.html'
    page_title = "MyPSE.ie - About"


class LearnMorePage(PageTitleMixin, generic.TemplateView):
    """
    Displays page that explains the benefits of the site
    and SEN Passports in general.
    """
    template_name = 'learn_more.html'
    page_title = "MyPSE.ie - Learn More"


class AddEnrolledPupil(PageTitleMixin, LoginRequiredMixin, SuccessMessageMixin,
                       generic.CreateView):
    """
    User with role of 'school' (admin) can add a
    pupil record to enrolled pupil table in database.
    """
    model = EnrolledPupil
    form_class = EnrolledPupilForm
    template_name = 'enrolled_pupil_form.html'
    page_title = "MyPSE.ie - Add Pupil Record"
    success_url = reverse_lazy('enrolled_pupil_list')
    success_message = "Pupil record added successfully!"

    def form_valid(self, form):
        """
        Auto applies foreign key and auto generated settings.
        """
        form.instance.created_by = self.request.user
        return super(AddEnrolledPupil, self).form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.add_message(self.request, messages.ERROR,
                             "Invalid form input... See errors below")
        return self.render_to_response(self.get_context_data(form=form))


class EnrolledPupilList(PageTitleMixin, LoginRequiredMixin, generic.ListView):
    """
    Displays page that lists pupil records created by logged in user
    """
    model = EnrolledPupil
    template_name = 'enrolled_pupil_list.html'
    page_title = "MyPSE.ie - Pupil List"
    context_object_name = 'enrolled_pupil_list'
    paginate_by = 9

    def get_queryset(self):
        return EnrolledPupil.objects.filter(
            created_by=self.request.user
        )


class EnrolledPupilRecord(PageTitleMixin, LoginRequiredMixin, View):
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
                "page_title": "MyPSE.ie - Pupil Record"
            },
        )


class UpdatePupilRecord(PageTitleMixin, LoginRequiredMixin,
                        SuccessMessageMixin, generic.edit.UpdateView):
    """
    User with role of School Admin can update enrolled existing pupil record
    """
    model = EnrolledPupil
    form_class = EnrolledPupilForm
    template_name = 'enrolled_pupil_form.html'
    page_title = "MyPSE.ie - Edit Pupil Record"
    success_url = reverse_lazy('enrolled_pupil_list')
    success_message = "Pupil record updated successfully!"

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.add_message(self.request, messages.ERROR,
                             "Invalid form input... See errors below")
        return self.render_to_response(self.get_context_data(form=form))


class DeletePupilRecord(PageTitleMixin, LoginRequiredMixin,
                        SuccessMessageMixin, generic.DeleteView):
    """
    User with role of School Admin can delete existing pupil record
    """
    model = EnrolledPupil
    success_url = reverse_lazy('enrolled_pupil_list')
    page_title = "MyPSE.ie - Delete Pupil Record"
    success_message = "Pupil record deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePupilRecord, self).delete(request, *args, **kwargs)


class ValidatePupilId(PageTitleMixin, generic.ListView, SuccessMessageMixin):
    """
    Ensures Pupil is enrolled in system before a passport can be created
    """
    template_name = 'validate_pupil_id.html'
    model = EnrolledPupil
    page_title = "MyPSE.ie - Validate Pupil ID"

    def get_queryset(self):
        query = self.request.GET.get('pupil_id')
        if query:
            object_list = self.model.objects.filter(pupil_id__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class AddPassport(PageTitleMixin, LoginRequiredMixin, generic.CreateView):
    """
    User with role of parent and a valid pupil ID number can create a passport
    """
    model = Passport
    form_class = PassportForm
    template_name = 'passport_form.html'
    page_title = "MyPSE.ie - Add Passport"
    success_url = reverse_lazy('passport_list')

    def form_valid(self, form):
        """
        Auto applies foreign key and auto generated settings.
        """
        form.instance.created_by = self.request.user
        messages.add_message(self.request, messages.SUCCESS,
                             "Passport Successfully Created!")
        return super(AddPassport, self).form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.add_message(self.request, messages.ERROR,
                             "Invalid form input... See errors below")
        return self.render_to_response(self.get_context_data(form=form))


class PassportList(PageTitleMixin, LoginRequiredMixin, generic.ListView):
    """
    Displays page that lists any passports created by logged in user (parent)
    """
    model = Passport
    template_name = 'passport_list.html'
    page_title = "MyPSE.ie - Passport List"
    context_object_name = 'passport_list'
    paginate_by = 3

    def get_queryset(self):
        return Passport.objects.filter(
            created_by=self.request.user
        )


class PassportDetail(PageTitleMixin, LoginRequiredMixin, View):
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
                "page_title": "MyPSE.ie - Passport"
            },
        )


class UpdatePassport(PageTitleMixin, LoginRequiredMixin, SuccessMessageMixin,
                     generic.edit.UpdateView):
    """
    Authenticated user with authorisation can update passport information
    """
    model = Passport
    form_class = PassportForm
    template_name = 'passport_form.html'
    page_title = "MyPSE.ie - Edit Passport"
    success_url = reverse_lazy('passport_list')
    success_message = "Passport successfully updated!"

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.add_message(self.request, messages.ERROR,
                             "Invalid form input... See errors below")
        return self.render_to_response(self.get_context_data(form=form))


class DeletePassport(PageTitleMixin, LoginRequiredMixin, SuccessMessageMixin,
                     generic.DeleteView):
    """
    Authenticated user with authorisation can delete a passport
    """
    model = Passport
    success_url = reverse_lazy('passport_list')
    page_title = "MyPSE.ie - Delete Passport"
    success_message = "Passport successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS,
                             "Passport successfully deleted!")
        return super(DeletePassport, self).delete(request, *args, **kwargs)


class TeacherPassportList(PageTitleMixin, generic.ListView):
    """
    Displays list of pupil passports when corresponding teacher id is typed
    """
    model = Passport
    template_name = 'teacher_passport_list.html'
    page_title = "MyPSE.ie - Teacher Passport List"

    def get_queryset(self):
        query = self.request.GET.get('teacher_id')
        if query:
            object_list = self.model.objects.filter(
                teacher_id__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class TeacherValidatePupilId(PageTitleMixin, generic.ListView):
    """
    Ensures Teacher has access to Pupil ID  before a passport can be viewed
    """
    template_name = 'teacher_validate_pupil_id.html'
    page_title = "MyPSE.ie - Validate Pupil ID"
    model = Passport

    def get_queryset(self):
        print(self.request.GET)
        query = self.request.GET.get('pupil_id')
        if query:
            object_list = self.model.objects.filter(pupil_id__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class TeacherPassportDetail(PageTitleMixin, LoginRequiredMixin, View):
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
                "page_title": "MyPSE.ie - Passport"
            },
        )


class PupilCheck(PageTitleMixin, LoginRequiredMixin, generic.ListView):
    """
    Displays page that lists pupil records created by logged in user
    """
    model = Passport
    template_name = 'pupil_check.html'
    page_title = "MyPSE.ie - Pupil Passport List"

    context_object_name = 'pupil_check'

    def get_queryset(self):
        return Passport.objects.filter(
            created_by=self.request.user
        )


class TestView(generic.TemplateView):
    """
    Displays 500 error page when URL/500 is typed in browser (for testing)
    """
    template_name = '500.html'
    page_title = "MyPSE.ie - Home"


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


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /https://mypse.herokuapp.com/pupil_record",
        "Disallow: /https://mypse.herokuapp.com/passport_detail",
        "Disallow: /https://mypse.herokuapp.com/teacher_passport_detail",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
