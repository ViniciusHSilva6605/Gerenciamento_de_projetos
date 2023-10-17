from django.urls import path
from django.contrib.auth import views as auth_views
from todos import views
app_name = 'todos'


from todos.views import (

    CompanyListView,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
    CompanyDetailListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)

urlpatterns = [
    
    
    path("", CompanyListView.as_view(), name="todo_list"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    # Empresas
    path("companies/", CompanyListView.as_view(), name="company_list"),
    path("companies/create", CompanyCreateView.as_view(), name="company_create"),
    path("companies/update/<int:pk>", CompanyUpdateView.as_view(), name="company_update"),
    path("companies/delete/<int:pk>", CompanyDeleteView.as_view(), name="company_delete"),
    path("companies/<int:pk>/projects/", CompanyDetailListView.as_view(), name="company_detail_list"),

     # Projetos
    path("projects/create/<int:company_id>", ProjectCreateView.as_view(), name="project_create"),
    path("projects/update/<int:company_id>/<int:pk>", ProjectUpdateView.as_view(), name="project_update"),
    path('projects/delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
    
    
]

