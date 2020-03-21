"""Users models."""

#Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """ Profile model.

    Proxy model that the extends the base data with other information

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField( upload_to='users/pictures',blank=True,null=True)
    trained_in = models.CharField(max_length=200, blank = True)

    def __str__(self):
        """Return username."""
        return self.user.username