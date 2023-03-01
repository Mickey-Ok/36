from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.CharField(max_length=700)
    cover=models.CharField(max_length=100)

class individual(models.Model):
    category_name=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    type=models.CharField(max_length=700)
    yr_published=models.CharField(max_length=20)
    book_cover=models.CharField(max_length=100)
# Create your models here.
