from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# each class is a relation in the database
class Post(models.Model):
    # fields that the relation will have
    title = models.CharField(max_length=100)
    content = models.TextField()
    """
    don't use parenthesis for timezone.now as we don't want to call the function
    at that point - we just want to pass it in
    """
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Post deleted if user is deleted

    # Used to format posts objects when querying database
    def __str__(self):
        return self.title
