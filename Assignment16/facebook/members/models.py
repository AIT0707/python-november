from django.db import models

class Cities(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_date = models.DateField(null=True)

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_date = models.DateField(null=True)

class Friends(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_date = models.DateField(null=True)