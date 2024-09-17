from django.db import models

# Create your models here.

class Document(models.Model):
    """
        Назначение: Хранит информацию о документах кафедры.
        
        Поля:
            - title: Заголовок документа.
            - document_type: Тип документа (например, "учебный план", "отчет").
            - created_at: Дата создания документа.
            - updated_at: Дата последнего обновления документа.
            - file: Файл документа.
    """
    title:str = models.CharField(max_length=255, help_text="Заголовок документа")
    documentt_type:str = models.CharField(max_length=100, help_text="Тип документа (учебный план, отчет, и т. д.)")
    created_at:models.DateTimeField = models.DateTimeField(auto_now_add=True, help_text="Дата создания документа")
    updated_at:models.DateTimeField = models.DateField(auto_now_add=True, help_text="Дата последнего обновления документа")
    file:str = models.FileField(upload_to='documents/', help_text="Файйл документа")
    
    """"""
    def __str__(self) -> str:
        return self.title
    

class Category(models.Model):
    """
        Позволяет классифицировать документы по категориям.
        
        Поля:
            - name (str): Название категории.
    """
    name:str = models.CharField(max_length=100, help_text="Название категории")
    
    def __str__(self) -> str:
        return self.name


class DocumentVersion(models.Model):
    """
        Позволяет отслеживать версии документов.

        Поля:
            - document (ForeignKey): Связь с моделью Document.
            - version_number (int): Номер версии документа.
            - file (FileField): Файл версии документа.
            - created_at (datetime): Дата создания версии.
    """
    
    document:Document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='versions', help_text='Документ для версии')
    version_number:int = models.IntegerField(help_text="Номер версии документа")
    file:str = models.IntegerField(upload_to='documents_version/', help_text="Файл версии документа")
    created_at:models.DateTimeField = models.DateTimeField(auto_now_add=True, help_text="Дата создания версии")
    
    def __str__(self) -> str:
        return f"{self.document.title} - Версия {self.version_number}"