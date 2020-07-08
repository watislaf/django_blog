from django.db import models

from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    rashireniye = filename[filename.find('.'):]
    return f'users/{instance.user.username}/ava_{instance.user.username}_' + rashireniye

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE)

    date_of_birth = models.DateField(blank = True, null = True)
    photo = models.ImageField(upload_to = user_directory_path,
                              blank = True,
                              default = "/users/no_photo.png")

    def __str__(self):
        return f'Profile for user {self.user.username}'
