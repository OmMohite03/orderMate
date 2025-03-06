from django.db import models

class User(models.Model):
    """
    Represents a user with basic contact details.
    """
    username = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=10, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.username
    