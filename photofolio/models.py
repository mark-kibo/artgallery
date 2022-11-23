from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)

    def __str__(self):
        return self.username


photo_choices = (
    ('nature', 'n'), ('adventure', 'a'), ('people', 'p')
)


class ArtImages(models.Model):
    type = models.CharField(max_length=255)
    art_image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.type
