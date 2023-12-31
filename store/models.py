from django.db import models 
from django.urls import reverse
from category.models import CategoryModel


# Create your models here.


class ProductModel(models.Model):
   product_name         = models.CharField(max_length=500, unique=True)
   slug                 = models.SlugField(max_length=500, unique=True)
   description          = models.TextField(max_length=500, blank=True)
   price                = models.IntegerField()
   images               = models.ImageField(upload_to='photos/products')
   stock                = models.IntegerField()
   is_available         = models.BooleanField(default=True)
   category             = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
   created_date         = models.DateTimeField(auto_now_add=True)
   modified_date        = models.DateTimeField(auto_now=True)
   
   
   class Meta:
      verbose_name = 'Product'
      verbose_name_plural = 'Products'
   
   def __str__(self):
      return self.product_name
   
   
   def get_url(self):
      return reverse('product_details', args=[self.category.slug, self.slug])
   
   