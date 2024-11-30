from django.urls import path
from . import views

urlpatterns = [
    # Client Endpoints
    path('clients/', views.ClientListCreateView.as_view(), name='client-list-create'),
    # GET (list clients) and POST (create client)
    path('clients/<int:pk>/', views.ClientRetrieveUpdateDestroyView.as_view(), name='client-retrieve-update-destroy'),
    # GET, PUT/PATCH, DELETE (client details)

    # Project Endpoints
    path('projects/', views.ProjectListCreateView.as_view(), name='project-list-create'),
    # GET (list projects) and POST (create project)
    path('projects/assigned/', views.ProjectAssignedToUserView.as_view(), name='project-assigned-to-user'),
    # GET (assigned projects to logged-in user)
    path('projects/<int:id>/', views.ProjectDeleteView.as_view(), name='project-delete'),  # DELETE (delete project)
]
