from django.db import models

from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    rashireniye = filename[filename.find('.'):]
    return f'users/{instance.user.username}/ava_{instance.user.username}_' + rashireniye

class Contact(models.Model):
    user_from = models.ForeignKey('auth.User',
                                  related_name = 'from_user',
                                  on_delete = models.CASCADE)
    user_to = models.ForeignKey('auth.User',
                                related_name = 'to_user',
                                on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True,
                                   db_index = True)

    # Оформяелся подписочка вот так ->
    # user1 = User.objects.get(id = 1)
    # user2 = User.objects.get(id = 2)
    # Contact.objects.create(user_from = user1, user_to = user2)
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'

from django.contrib.auth import get_user_model

# Add following field to User dynamically
user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField('self', # связь с пользователями
                                               through = Contact, # через класс Contact
                                               related_name = 'followers',
                                               symmetrical = False)) #  (if I follow you, it doesn't mean that you automatically follow me).

# Подписочка
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE)

    date_of_birth = models.DateField(blank = True, null = True)
    photo = models.ImageField(upload_to = user_directory_path,
                              blank = True,
                              default = "/users/no_photo.png")

    def __str__(self):
        return f'Profile for user {self.user.username}'
