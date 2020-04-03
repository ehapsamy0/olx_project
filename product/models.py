from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from django.utils.text import slugify

class Product(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    CONDITION_TYPE = (
        ('New','New'),
        ('Used','Used'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=600)
    condition = models.CharField(max_length=100,choices=CONDITION_TYPE)
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,null=True,blank=True)
    brand = models.ForeignKey("Brand",on_delete=models.SET_NULL,null=True,blank=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='main_product/',null=True,blank=True)


    def __str__(self):
        return self.name



    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)

        super(Product,self).save(*args,**kwargs)

class ProductImages(models.Model):
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/',null=True,blank=True)



    class Meta:
        verbose_name = 'Product Images'
        verbose_name_plural = 'Product Images'



    def __str__(self):
        return '%s  image'%(self.product)




class Category(models.Model):
    category_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category/',blank=True,null=True)
    slug = models.SlugField(blank=True,null=True)
    icon_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name



    def save(self,*args,**kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)

        super(Category,self).save(*args,**kwargs)


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'Brand'

    def __str__(self):
        return self.brand_name

