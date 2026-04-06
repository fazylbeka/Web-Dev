from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)  # 👈 ВАЖНО
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name