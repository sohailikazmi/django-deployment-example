from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Following class will add functionality to user that the default user above does not have:
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional things for the User
    portfolio_site = models.URLField(blank=True) #blank so the user does not have to provide it.
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) # for this we need pillow libraray installed (pip3 install pillow)

    def __str__(self):
        return self.user.username
