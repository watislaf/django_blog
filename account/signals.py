from django.db import models
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender = User)
# автоматически присваивает число лайкам
def create_user_profile(sender, instance, created, **kwargs):
    user_ = instance
    if Profile.objects.all().filter(user = user_).count() == 0:
        profile = Profile(user = user_)
        profile.save()