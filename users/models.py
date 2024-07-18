from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', default="image\403019_avatar_male_man_person_user_icon.png", blank=True)

    def __str__(self):
        return self.user.username