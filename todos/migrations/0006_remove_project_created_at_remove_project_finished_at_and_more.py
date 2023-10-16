# Generated by Django 4.2.1 on 2023-10-16 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0005_project_finished_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='project',
            name='finished_at',
        ),
        migrations.AlterField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companies', models.ManyToManyField(related_name='memberships', to='todos.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
