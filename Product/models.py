import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=80,db_index=True)
    slug = models.SlugField(max_length=150,unique=True,db_index=True)
    price = models.DecimalField(max_digits=1000,decimal_places=2)
    hight = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image/', height_field='hight', width_field='width', max_length=100)
    store = models.PositiveIntegerField()
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='Brand', null=True,blank=True)
    author = models.CharField(max_length=30,null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_product_available(self):
        return self.store>1
    
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_at <= now
    was_published_recently.admin_order_field = 'created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[str(self.id), self.slug])
