from django.contrib import admin
from .models import EnrolledPupil, Passport
from django_summernote.admin import SummernoteModelAdmin


@admin.register(EnrolledPupil)
class EnrolledPupilAdmin(admin.ModelAdmin):
    list_display = ('pupil_full_name',
                    'school_name', 'pupil_id', 'school_email',
                    'created_by')
    search_fields = ('pupil_full_name',
                     'school_name', 'pupil_id', 'school_email',
                     'created_by')


@admin.register(Passport)
class PassportAdmin(SummernoteModelAdmin):
    list_display = ('my_full_name',
                    'my_emergency_contact_name',
                    'my_emergency_contact_number',
                    'slug', 'my_date_of_birth',
                    'created_by', 'last_updated'
                    )
    search_fields = ('my_full_name',
                     'my_emergency_contact_name',
                     'my_emergency_contact_number',
                     'slug', 'my_date_of_birth',
                     'created_by', 'last_updated'
                     )
