from django.urls import path
from .views import document_list, document_create


urlpatterns = [
    path('', document_list, name='document_list'),
    path('create/', document_create, name='documents_create'),
]
