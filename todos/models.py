from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone




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
    def __str__(self):
        return self.user.username


