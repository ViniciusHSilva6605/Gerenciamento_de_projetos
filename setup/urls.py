from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from todos.views import TodoListView
from django.urls import path, include


from todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
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
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Inclui as URLs de autenticação embutidas
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
    
    # Empresas
    path("companies/", CompanyListView.as_view(), name="company_list"),
    path("companies/create", CompanyCreateView.as_view(), name="company_create"),
    path("companies/update/<int:pk>", CompanyUpdateView.as_view(), name="company_update"),
    path("companies/delete/<int:pk>", CompanyDeleteView.as_view(), name="company_delete"),
    path("companies/<int:pk>/projects/", CompanyDetailListView.as_view(), name="company_detail_list"),

     # Projetos
    path("projects/create/<int:company_id>", ProjectCreateView.as_view(), name="project_create"),
    path("projects/update/<int:company_id>/<int:pk>", ProjectUpdateView.as_view(), name="project_update"),
    path("projects/delete/<int:company_id>/<int:pk>", ProjectDeleteView.as_view(), name="project_delete"),
    
    
]

