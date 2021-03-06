from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Grape(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Wine(models.Model):
    product_code = models.CharField(max_length=254, null=True, blank=True) # Optional field
    name = models.CharField(max_length=254) # Mandatory Field
    description = models.TextField() # Mandatory Field
    country = models.CharField(max_length=254) # Mandatory Field
    grape = models.ForeignKey('Grape', null=True, blank=True, on_delete=models.SET_NULL) # Optional field  
    price = models.DecimalField(max_digits=6, decimal_places=2) # Mandatory Field
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL) # Optional field
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True) # Optional field
    image = models.ImageField(null=True, blank=True) # Optional field

    def __str__(self):
        return self.name
        
