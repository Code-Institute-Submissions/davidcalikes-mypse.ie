from django.db import models
from django.contrib.auth.models import AbstractUser


TYPE_CHOICES = (
               ("pupil", "pupil"),
               ("parent", "parent"),
               ("teacher", "teacher"),
               ("school", "school"),
                    )


class CustomUser(AbstractUser):
    """
    Adds extra 'role' field to user model that helps assign specific
    priveliges to different types of user
    """
    role = models.CharField(choices=TYPE_CHOICES, max_length=20)
