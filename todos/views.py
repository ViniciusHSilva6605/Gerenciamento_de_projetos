from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Todo, Company, Project
from django.contrib.auth.views import LoginView
import os
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Company
from django.contrib.auth.models import User

directory = os.path.dirname(os.getcwd())



    
class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")
    


# Visualização para listar todas as empresas do usuário logado
class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.all()  # Adicione a lista de projetos ao contexto
        return context



class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'creator'] 
    template_name = 'todos/company_form.html'  # Atualize o caminho do template aqui
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.creator = User.objects.first()  # Defina o criador como o primeiro usuário
        return super().form_valid(form)


# Visualização para atualizar uma empresa
class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['name']
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
    fields = ['name']
    template_name = "todos/"
    #Criar template project_update.html
    def get_success_url(self):
        return reverse_lazy('company_detail_list', kwargs={'pk': self.kwargs['company_id']})

# Visualização para excluir um projeto (adicionar lógica de autorização necessária)

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "todos/project_delete.html"
   

    def get_success_url(self):
        return reverse_lazy('company_detail_list', kwargs={'pk': self.kwargs['company_id']})



