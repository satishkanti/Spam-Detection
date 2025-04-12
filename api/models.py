from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model inheriting from AbstractUser to add additional fields
class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)


# Contact model to store contact information
class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return self.name
