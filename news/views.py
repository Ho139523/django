from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Articles, Category

def home(request, page=1):
    article_list = Articles.objects.filter(status='p')
    paginator = Paginator(article_list, 4)
    page_obj = paginator.get_page(page)
    data={
        'Articles': page_obj
    }
    return render(request, 'news/home.html', context=data)

def description(request, slug):
    data={
        'Article': get_object_or_404(Articles, slug=slug, status='p')
    }
    return render(request, 'news/description.html', context=data)

def category(request, slug, page=1):
    article_list = get_object_or_404(Category, slug=slug, status=True).articles.published()
    paginator = Paginator(article_list, 4)
    page_obj = paginator.get_page(page)
    data={
        'Categories': get_object_or_404(Category, slug=slug, status=True),
        'Articles': page_obj,
    }
    return render(request, 'news/category.html', context=data)
