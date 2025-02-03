from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True, null = False, blank = False)
    emailAddress = models.EmailField(max_length=255, unique=True, null = False, blank = False)
    phoneNumber = models.CharField(max_length=10, unique=True, null = True, blank = True)
    address  = models.TextField (null = True, blank = True)

    is_active  = models.BooleanField (default=True)

    createdBy = models.CharField(max_length=255, null = False, default = username)
    createdOn = models.DateTimeField(null = True, auto_now_add=True)
    modifiedBy = models.CharField(max_length=255, null = True, default= "yet to be modified")
    modifiedOn = models.DateTimeField(null = True)

    def __str__(self):
        return self.username