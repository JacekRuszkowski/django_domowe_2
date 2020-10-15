from django.db import models
from django.urls import reverse


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    is_available = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

