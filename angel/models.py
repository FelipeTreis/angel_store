from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Unisex', 'Unisex')
    )
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES,
        blank=False, null=False, default='Unisex')
    length = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    qty_parcel = models.IntegerField(null=True, blank=True)
    value_parcel = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00, null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title
