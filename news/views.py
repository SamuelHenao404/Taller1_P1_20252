from django.shortcuts import render
from .models import News

def index(request):
    news_items = News.objects.all().order_by('-date')
    return render(request, 'news/index.html', {'news_items': news_items})

