from django.contrib import admin
from .models import EnrolledPupil, Passport


@admin.register(EnrolledPupil)
class EnrolledPupilAdmin(admin.ModelAdmin):
    list_display = ('pupil_full_name',
                    'school_name', 'pupil_id', 'school_email',
                    'created_by', 'last_updated')
    search_fields = ('pupil_full_name',
                     'school_name', 'pupil_id', 'school_email',
                     'created_by', 'last_updated')


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('my_full_name',
                    'my_emergency_contact_name',
                    'my_emergency_contact_number',
                    'slug', 'my_date_of_birth', 'my_biography',
                    'my_family', 'my_likes', 'my_dislikes', 'my_strengths',
                    'my_difficulties', 'my_supports', 'my_calming_measures',
                    'my_communication_skills', 'my_other_info',
                    'created_by', 'last_updated'
                    )
    search_fields = ('my_full_name',
                     'my_emergency_contact_name',
                     'my_emergency_contact_number',
                     'slug', 'my_date_of_birth', 'my_biography',
                     'my_family', 'my_likes', 'my_dislikes', 'my_strengths',
                     'my_difficulties', 'my_supports', 'my_calming_measures',
                     'my_communication_skills', 'my_other_info',
                     'created_by', 'last_updated'
                     )
