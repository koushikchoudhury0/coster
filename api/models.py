from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Ingredient(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(unique = True, max_length = 50)
    uom = models.IntegerField()
    cost = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        db_table = 'ingredient'
        managed = False

class Product(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(unique = True, max_length = 50)
    total = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        db_table = 'product'
        managed = False

class MapIngredientProduct(models.Model):
    ingredient_id=models.IntegerField()
    product_id=models.IntegerField()
    unit=models.IntegerField()
    rate=models.IntegerField()
    total=models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table="map_ingredient_product"
        managed = False



class Raw(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()