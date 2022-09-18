from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=30)

    def create(self, validated_data):
        print("Created Method Called")
        return Employee.objects.create(**validated_data)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    date_joined = serializers.CharField(max_length=30)
