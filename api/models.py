from django.db import models

# Create your models here.

def casamento_path(instance, filename):
    return f'casamento/{filename}'

class Casamento(models.Model):
    image = models.ImageField(upload_to=casamento_path)
    approved = models.BooleanField(default=False, null=False, blank=True)
