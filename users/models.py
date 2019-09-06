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

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)