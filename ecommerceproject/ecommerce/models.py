from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    cdesc = models.TextField(blank=True)
    cimage = models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('cname',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.cname)

    def get_url(self):
        return reverse('ecommerce:products_by_category',args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product',blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    stock = models.IntegerField()
    balance = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('ecommerce:prodetail',args=[self.category.slug, self.slug])