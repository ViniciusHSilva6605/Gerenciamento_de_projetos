from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import  Company, Project, User
from django.views.generic.edit import CreateView
from .models import Company
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.messages import constants
from django.http import HttpResponse
from hashlib import sha256
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView

from .forms import LoginForm, RegisterForm

from django.contrib.auth import login
from django.contrib import messages

class LoginView(FormView):
    template_name = 'todos/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('company_list')  # Substitua 'company_list' pela URL desejada
        else:
            messages.error(self.request, 'Usuário ou senha incorretos.')
            return super().form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class RegisterView(FormView):
    template_name = 'todos/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Registro bem-sucedido. Agora você pode fazer login.')
        return super().form_valid(form)

# Visualização para listar todas as empresas do usuário logado
class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.all() 
        return context



class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'creator'] 
    #template_name = 'todos/company_form.html'  
    success_url = reverse_lazy('todo_list')

    #def form_valid(self, form):
    #    form.instance.creator = Username.objects.first()  # Defina o criador como o primeiro usuário
    #    return super().form_valid(form)


# Visualização para atualizar uma empresa
class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name', 'creator']
    template_name = "todos/company_update.html"
    success_url = reverse_lazy('todo_list')

# Visualização para excluir uma empresa (adicionar lógica de autorização necessária)
class CompanyDeleteView(DeleteView):
    model = Company
    template_name = "todos/company_delete.html"
    #Criar template company_delete.html
    success_url = reverse_lazy('todo_list')

# Visualização para listar os projetos de uma empresa
class CompanyDetailListView(ListView):
    model = Project
    template_name = "todos/company_detail_list.html"
    def get_queryset(self):
        return Project.objects.filter(company__id=self.kwargs['pk'])


# Visualização para criar um novo projeto para uma empresa (adicionar lógica de autorização necessária)
class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'creator', 'company', 'members']
    template_name = "todos/project_form.html"
    success_url = reverse_lazy('todo_list')
    #def get_success_url(self):
    #    return reverse_lazy('company_detail_list', kwargs={'pk': self.kwargs['company_id']})


# Visualização para atualizar um projeto (adicionar lógica de autorização necessária)
class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name','creator','company','members']
    template_name = "todos/project_update.html"
    def get_success_url(self):
        return reverse_lazy('company_detail_list', kwargs={'pk': self.kwargs['company_id']})

# Visualização para excluir um projeto (adicionar lógica de autorização necessária)

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'todos/project_delete.html'

    def get_success_url(self):
        # Use reverse to generate the URL based on the name of the URL pattern.
        return reverse('company_detail_list', kwargs={'pk': self.object.company.id})

