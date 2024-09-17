from django.contrib import admin
from .models import Document, Category, DocumentVersion


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('titile', 'document_type', 'created_at', 'updated_at')
    search_fields = ('title', 'document_type')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ('name')


@admin.register(DocumentVersion)
class DocumentVersionAdmin(admin.ModelAdmin):
    list_display = ('document', 'version_number', 'created_at')
    search_fields = ('document__titile')
