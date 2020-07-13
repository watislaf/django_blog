from django.contrib.auth.models import User
from .models import Profile

# собственный обьект для авторизации. Если Джанго не может авторизовать по одному беку, то он идёт к другому.
# тут идёт бек с почтой, для этого надо переопределить два метода authenticate,get_user
from social_core.backends.vk import VKOAuth2
from django.core import files
from io import BytesIO
import requests

class MyVk(VKOAuth2):
    def get_user_details(self, response):
        if response["nickname"] != None and response["nickname"] == '':
            name = response["screen_name"]
            user_ = User.objects.all().filter(username = name)[0]
            if Profile.objects.all().filter(user = user_).count() == 0:
                profile = Profile(user = user_)
                url = response["photo"]
                resp = requests.get(url)
                fp = BytesIO()
                fp.write(resp.content)
                profile.photo.save('.png', files.File(fp))
                profile.save()

        return super().get_user_details(response)
