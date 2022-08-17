from dataclasses import fields
from rest_framework import serializers
from .models import UserD

class MyAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = UserD
        fields = ['id', 'fname', 'lname', 'email', 'phone','add_line1', 'add_line2', 'city', 'zipcode', 'state']

