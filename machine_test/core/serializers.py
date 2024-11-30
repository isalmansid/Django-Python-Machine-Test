from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

# Nested User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  # Include the fields you want, e.g., id and name

# Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Client
        fields = '__all__'  # Include all fields from the Client model

# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    # Retrieve the client name
    client_name = serializers.CharField(source='client.client_name', read_only=True)

    # Retrieve the username of the user who created the project
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    # Include users as a nested list with id and username
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client_name', 'users', 'created_at', 'created_by']
