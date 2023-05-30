from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=64)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Personnel(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    TITLE = (
        ('S', 'Senior Level'),
        ('M', 'Mid level'),
        ('J', 'Junior Level'),
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=GENDER)
    title = models.CharField(max_length=1, choices=TITLE)
    salary = models.IntegerField()
    started = models.DateField()
    department_id = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, related_name='personnel')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
    