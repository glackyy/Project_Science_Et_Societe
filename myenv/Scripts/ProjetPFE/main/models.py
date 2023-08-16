from django.db import models
from django.contrib.auth.models import AbstractUser

class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)

class UserProfile(AbstractUser):
    custom_field = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',)

    def __str__(self):
        return self.username


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
