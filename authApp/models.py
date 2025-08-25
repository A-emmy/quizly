from django.db import models
from django.contrib.auth.models import User
# the above helps us create a user schema since its already a model created in django
# Create your models here.
# the model helps Create a schema in the database......

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # this is a one to one relationship this means that the user has one profile and the profile has one user
    bio = models.TextField()
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

      