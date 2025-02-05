from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User




# view one
# api_view(['GET'])
# def view_one(req):


# view all
@api_view(['GET'])
def view_all(req):
    users = User.objects.filter(is_active = True)
    if users:
        serializers = UserSerializer(users, many = True)
        return Response({
            'msg': 'users listed',
            'users': serializers.data,
        },status.HTTP_200_OK)
    else:
        return Response(status.HTTP_404_NOT_FOUND)


# add
@api_view(['POST'])
def add(req):
    data = {}

    username = req.data.get('username')
    emailAddress = req.data.get('emailAddress')
    phoneNumber = req.data.get('phoneNumber')
    address = req.data.get('address')

    data = {
        'username': username,
        'emailAddress': emailAddress,
        'phoneNumber': phoneNumber,
        'address': address,
    }

    if 'is_active' not in data:
        data['is_active'] = True

    if 'createdBy' not in data:
        data['createdBy'] = 'username'
    
    if 'modifiedBy' not in data:
        data['modifiedBy'] = 'yet to be modified'

    userSerializer = UserSerializer(data = data)
    if userSerializer.is_valid():
        userSerializer.save()
        return Response({
            'msg': 'user created',
            'users': userSerializer.data,
        },status.HTTP_201_CREATED)
    else:
        return Response(status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def update(req):
    data = {}

    data['id'] = req.data.get('id')
    data['username'] = req.data.get('username')
    data['emailAddress'] = req.data.get('emailAddress')
    data['phoneNumber'] = req.data.get('phoneNumber')
    data['address'] = req.data.get('address')
    data['modifiedBy'] = req.data.get('username')
    data['modifiedOn'] = datetime.now()

    usersObj = User.objects.filter(id = data['id']).first()
    userSerializer = UserSerializer(usersObj, data = data)

    if userSerializer.is_valid():
        userSerializer.save()
        return Response(userSerializer.data)
    else:
        return Response(userSerializer.errors)
    

@api_view(['POST']) 
def delete(req, id):
    data = {}
    data['id'] = req.data.get('id')
    users = get_object_or_404(User, id=data['id'])
    users.is_active = False
    users.save()
    return Response({'msg': 'deleted!'}, status.HTTP_200_OK)