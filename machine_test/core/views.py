from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# Client Views

# View to list all clients and create a new client
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the 'created_by' to the logged-in user
        serializer.save(created_by=self.request.user)

# View to retrieve, update, or delete a specific client
class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

# Project Views

# View to list all projects and create a new project
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Retrieve the client by its ID from the request data
        client_id = self.request.data.get('client_id')
        client = get_object_or_404(Client, id=client_id)  # Will raise 404 if the client does not exist

        # Retrieve the list of user IDs from the request data
        user_ids = self.request.data.get('users', [])
        users = User.objects.filter(id__in=user_ids)  # Query for users by ID

        # If some users don't exist, raise a NotFound exception with their IDs
        if len(users) != len(user_ids):
            missing_users = set(user_ids) - set(users.values_list('id', flat=True))
            raise NotFound(f"Users with IDs {missing_users} not found.")

        # Save the project with the assigned client, users, and set the logged-in user as the creator
        project = serializer.save(client=client, created_by=self.request.user)
        project.users.set(users)  # Assign users to the project

# View to list all projects assigned to the logged-in user
class ProjectAssignedToUserView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return projects assigned to the logged-in user
        return self.request.user.projects.all()

# View to delete a project by ID
class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'  # Match project ID
