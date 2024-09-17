from django.db import models

# Create your models here.

class Documents(models.Model):
    title:str = models.CharField(max_length=255, help_text="Заголовок документа")


