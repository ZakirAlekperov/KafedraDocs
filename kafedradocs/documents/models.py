from django.db import models

# Create your models here.

class Documents(models.Model):
    title:str = models.CharField(max_length=255, help_text="Заголовок документа")
    documentt_type:str = models.CharField(max_length=100, help_text="Тип документа (учебный план, отчет, и т. д.)")
    created_at:models.DateTimeField = models.DateTimeField(auto_now_add=True, help_text="Дата создания документа")
    updated_at:models.DateTimeField = models.DateField(auto_now_add=True, help_text="Дата последнего обновления документа")
    file:str = models.FileField(upload_to='documents/', help_text="Файйл документа")
    
    
    def __str__(self) -> str:
        return self.title
    

class Category(models.Model):
    name:str = models.CharField(max_length=100, help_text="Название категории")
    
    def __str__(self) -> str:
        return self.name


