from django.db import models

# Create your models here.
class Category(models.Model):
    '''
    Represents a category.

    Attributes:
        name (str): The name of the category.
    '''
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    '''
    Represents a tag.

    Attributes:
        name (str): The name of the tag.
    '''
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    '''
    Represents a product.

    Attributes:
        name (str):             The name of the product.
        description (str):      The product descroption.
        category (Category):    What category the product as associated with
        tags (QuerySet[Tag]):   The tags related to the product
    '''
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
