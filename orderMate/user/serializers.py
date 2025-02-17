from datetime import timezone
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'emailAddress',
            'phoneNumber',
            'address',

            'createdBy',
            'createdOn',
            'modifiedBy',
            'modifiedOn'
            ]