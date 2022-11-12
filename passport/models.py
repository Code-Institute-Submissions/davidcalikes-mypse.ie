from django.db import models
from user.models import CustomUser
from cloudinary.models import CloudinaryField
from django.core.validators import RegexValidator
from django.utils.text import slugify


class EnrolledPupil(models.Model):

    pupil_full_name = models.CharField(
        "Pupil's Full Name", max_length=200, default="")
    pupil_id = models.CharField(
        "Pupil ID Number",
        validators=[RegexValidator(r'^[1-9]{1}[0-9]{7}$',
                    message="Not a valid pupil id number")],
        max_length=8, default="", unique=True)
    school_name = models.CharField(
       "School Name", max_length=200, default="")
    school_roll_number = models.CharField(
        "School Roll No",
        validators=[RegexValidator(r'^\d{5}[A-Z]{1}$',
                    message="Not a valid School Roll Number")],
        max_length=6, default="")
    school_email = models.EmailField(
        "School Email Address", max_length=300)
    created_by = models.ForeignKey(CustomUser,
                                   on_delete=models.CASCADE,
                                   related_name="created_by")

    def __int__(self):
        return self.pupil_id


class Passport(models.Model):

    pupil_id = models.CharField(
        "Pupil ID Number",
        validators=[RegexValidator(r'^[0-9]{8}$',
                    message="Not a valid pupil id number")],
        max_length=8, unique=True)
    teacher_id = models.CharField(
        "Teacher ID Number",
        validators=[RegexValidator(r'^[0-7]{6}$',
                    message="Not a valid Teacher ID")],
        max_length=6, default="")
    slug = models.SlugField(
        max_length=200, unique=True, default="")
    my_full_name = models.CharField(
        "Pupil's Full Name", max_length=200,)
    my_passport_image = CloudinaryField(
        "Passport Photo", default="placeholder")
    my_emergency_contact_name = models.CharField(
        "Emergency Contact Name", max_length=200, default='')
    my_emergency_contact_number = models.CharField(
        "Emergency Contact Number", max_length=100, default='')
    my_date_of_birth = models.DateField(
        "Pupil's Date Of Birth", default="YYYY-MM-DD", blank=False)
    my_biography = models.TextField(
       "Biography", max_length=1000, blank=False)
    my_family = models.TextField(
        "Family", max_length=1000, blank=False)
    my_family_image = CloudinaryField(
        "Family Photo", default="placeholder")
    my_likes = models.TextField(
       "Likes", max_length=1000, blank=False)
    my_likes_image = CloudinaryField(
        "Likes Photo", default="placeholder")
    my_dislikes = models.TextField(
        "Dislikes", max_length=1000, blank=False)
    my_strengths = models.TextField(
       "Strengths", max_length=1000, blank=False)
    my_difficulties = models.TextField(
        "Difficulties", max_length=1000, blank=False)
    my_supports = models.TextField(
        "Supports", max_length=1000, blank=False)
    my_supports_image = CloudinaryField(
        "Supports Photo", default="placeholder")
    my_calming_measures = models.TextField(
       "Calming Measures", max_length=1000, blank=False)
    my_communication_skills = models.TextField(
        "Communication Skills", max_length=1000, blank=False)
    my_communication_skills_image = CloudinaryField(
        "Communication Skills Photo", default='placeholder')
    my_other_info = models.TextField(
       "Other Info", max_length=1000, blank=False)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser,
                                   on_delete=models.CASCADE,
                                   related_name="creator")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pupil_id)
        super(Passport, self).save(*args, **kwargs)

    def __str__(self):
        return self.my_full_name
