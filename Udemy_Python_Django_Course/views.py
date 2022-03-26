from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = 'Hello World'
    text = 'Новая страница'
    return render(request, './index.html', {
        'a': a,
        'text': text
    })