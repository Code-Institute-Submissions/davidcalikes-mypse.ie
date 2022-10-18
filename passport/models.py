from django.db import models
from user.models import CustomUser
from cloudinary.models import CloudinaryField


class EnrolledPupil(models.Model):
    pupil_last_name = models.CharField(
        max_length=200, default='')
    pupil_first_name = models.CharField(
        max_length=200, default='')
    school_name = models.CharField(
        max_length=200, default='')
    teacher_name = models.CharField(
        max_length=200, default='')
    school_roll_no = models.CharField(
        max_length=200, default='')
    pupil_id = models.PositiveIntegerField(
        default=0, unique=True)
    school_email = models.EmailField(max_length=200)
    created_by = models.ForeignKey(CustomUser,
                                   on_delete=models.CASCADE,
                                   related_name='created_by')
    last_updated = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.pupil_id


class Passport(models.Model):
    my_full_name = models.CharField(
        max_length=200,)
    my_passport_image = CloudinaryField('image', default='placeholder')
    my_emergency_contact_one_name = models.CharField(
        max_length=200, default='')
    my_emergency_contact_one_number = models.PositiveIntegerField(
        default=0,)
    slug = models.SlugField(
        max_length=200, unique=True, default='')
    my_emergency_contact_two_name = models.CharField(
        max_length=200, default='')
    my_emergency_contact_two_number = models.PositiveIntegerField(
        default=0,)
    my_date_of_birth = models.DateField(
        default='DD/MM/YY', blank=False)
    my_biography = models.TextField(
        max_length=600, blank=False)
    my_family = models.TextField(
        max_length=600, blank=False)
    my_likes = models.TextField(
        max_length=600, blank=False)
    my_dislikes = models.TextField(
        max_length=600, blank=False)
    my_strengths = models.TextField(
        max_length=600, blank=False)
    my_difficulties = models.TextField(
        max_length=600, blank=False)
    my_supports = models.TextField(
        max_length=600, blank=False)
    my_calming_measures = models.TextField(
        max_length=600, blank=False)
    my_communication_skills = models.TextField(
        max_length=600, blank=False)
    my_other_info = models.TextField(
        max_length=600, blank=False)
    teacher_id = models.CharField(
        max_length=50, default='')
    pupil_id = pupil_id = models.PositiveIntegerField(
        default=0, unique=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser,
                                   on_delete=models.CASCADE,
                                   related_name='creator')
    my_family_image = CloudinaryField('image', default='placeholder')
    my_favorite_image = CloudinaryField('image', default='placeholder')
    my_hobby_image = CloudinaryField('image', default='placeholder')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pupil_id)
        super(Passport, self).save(*args, **kwargs)

    def __str__(self):
        return self.my_full_name
