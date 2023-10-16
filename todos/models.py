from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Todo(models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega", null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()







class Company(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)  # Define um valor padrão usando a data e hora atual
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    companies = models.ManyToManyField(Company, related_name='memberships')


