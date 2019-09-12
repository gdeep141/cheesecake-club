from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # If the user is deleted the profile is deleted, but not vice-versa
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Uploaded images are saved to 'profile_pics' directory
    image = models.ImageField(default='illusion.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.username + " Profile"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        base_size = 300
        if img.height > base_size or img.width > base_size:
            img.thumbnail((base_size, base_size), Image.ANTIALIAS)
            img.save(self.image.path)
        