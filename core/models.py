from django.db import models

# SIGNALS.
from django.db.models import signals
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Base(models.Model):
    created = models.DateTimeField('data criacao', auto_now_add=True)
    updated = models.DateTimeField('data atualizacao', auto_now=True)
    activated = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    name = models.CharField('Nome', max_length=50)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    stock = models.IntegerField('Estoque')

    image = models.ImageField(
        'Imagem', upload_to='images/produtos/%y/%m/%d')

    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name


@receiver(signals.pre_save, sender=Produto)
def produto_pre_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
