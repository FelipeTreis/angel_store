from brand.models import Brand
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Clothes(models.Model):
    class Meta:
        verbose_name = 'Roupa'
        verbose_name_plural = 'Roupas'
        ordering = ('-created_at',)

    GENDER_CHOICES = (
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Unisex', 'Unisex')
    )
    title = models.CharField('Título', max_length=65)
    description = models.CharField('Descrição', max_length=165)
    gender = models.CharField(
        'Gênero', max_length=9, choices=GENDER_CHOICES,
        blank=False, null=False, default='Unisex')
    length = models.CharField('Tamanho', max_length=100)
    value = models.DecimalField(
        'Valor', max_digits=6, decimal_places=2, default=0.00)
    qty_parcel = models.IntegerField(
        'Quantidade de Parcelas', null=True, blank=True)
    value_parcel = models.DecimalField(
        'Valor das Parcelas', max_digits=6, decimal_places=2,
        default=0.00, null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizaco em', auto_now=True)
    is_published = models.BooleanField('Está publicado', default=False)
    cover = models.ImageField(
        'Imagem', upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(
        Category,  on_delete=models.SET_NULL, null=True,
        blank=True, default=None,
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    brands = models.ManyToManyField(Brand)

    def __str__(self):
        return self.title
