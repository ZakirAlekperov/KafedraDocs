from django.db import models

# Create your models here.

class Document(models.Model):
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


class DocumentVersion(models.Model):
    document:Document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='versions', help_text='Документ для версии')
    version_number:int = models.IntegerField(help_text="Номер версии документа")
    file:str = models.IntegerField(upload_to='documents_version/', help_text="Файл версии документа")
    created_at:models.DateTimeField = models.DateTimeField(auto_now_add=True, help_text="Дата создания версии")
    
    def __str__(self) -> str:
        return f"{self.document.title} - Версия {self.version_number}"