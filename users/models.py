from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # If the user is deleted the profile is deleted, but not vice-versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Uploaded images are saved to 'profile_pics' directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username + " Profile"

    def save(self):
        super().save()
        