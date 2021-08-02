from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    undated_at = models.DateTimeField(auto_now=True)