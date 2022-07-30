import string
from random import SystemRandom

from django.db import models
from django.utils.text import slugify


class Brand(models.Model):
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    brand = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            rand_letters = ''.join(
                SystemRandom().choices(
                    string.ascii_letters + string.digits,
                    k=5,
                )
            )
            self.slug = slugify(f'{self.brand}-{rand_letters}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.brand
