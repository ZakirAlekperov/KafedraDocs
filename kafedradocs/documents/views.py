from django.shortcuts import render, get_object_or_404, redirect
from .models import Document
from .forms import DocumentForm


def document_list(request):
    """
        Отображает список всех документов.

        Параметры:
            request (HttpRequest): Объект запроса Django.

        Возвращает:
            HttpResponse: Рендеринг шаблона с контекстом документов.
    """
    documents = Document.objects.all()
    return render(request, 'documents/documents_list.html', {'documents':documents})


def document_create(request):
    """
        Создает новый документ.

        Параметры:
            request (HttpRequest): Объект запроса Django.

        Возвращает:
            HttpResponse: Рендеринг шаблона формы или перенаправление на список документов.
    """
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'documents/document_form.html', {'form': form})