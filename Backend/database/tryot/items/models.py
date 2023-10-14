from django.db import models
from django.contrib.postgres import fields as PostgresFields

class Category(models.Model):
    name = models.CharField(max_length=64)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    GENDER_TYPE = [
        ("M", "Male"),
        ("F", "Female"),
        ("U", "Unisex"),
    ]

    name = models.CharField(max_length=256)
    description = models.CharField(max_length = 4096)

    category_id = models.ForeignKey(
        Category,
        related_name="items",
        on_delete=models.CASCADE
    )

    brand_id = models.ForeignKey(
        Brand,
        blank=True,
        null=True,
        related_name="items",
        on_delete=models.CASCADE,
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

    image_url = models.URLField(blank=True, null=True)
    order_url = models.URLField(blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER_TYPE, default="U")
    material = PostgresFields.ArrayField(
        models.CharField(max_length=32),
        blank=True,
        null=True,
    )
    color = PostgresFields.ArrayField(
        models.CharField(max_length=32),
        blank=True,
        null=True,
    ) 

    feature_vector = PostgresFields.ArrayField(
        models.FloatField(),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.itemName
