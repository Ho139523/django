from django.shortcuts import render, get_object_or_404
from accounts.models import User
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Articles, Category

# def home(request, page=1):
#     article_list = Articles.objects.filter(status='p')
#     paginator = Paginator(article_list, 4)
#     page_obj = paginator.get_page(page)
#     data={
#         'Articles': page_obj
#     }
#     return render(request, 'news/home.html', context=data)

class Home(ListView):
    template_name='news/home.html'
    queryset=Articles.objects.published()
    context_object_name='Articles'
    paginate_by=4


# def description(request, slug):
#     data={
#         'Article': get_object_or_404(Articles, slug=slug, status='p')
#     }
#     return render(request, 'news/description.html', context=data)

class Description(DetailView):
    template_name='news/description.html'
    def get_object(self):
        slug=self.kwargs.get('slug')
        return get_object_or_404(Articles, slug=slug, status='p')
    context_object_name='Article'

# def category(request, slug, page=1):
#     article_list = get_object_or_404(Category.objects.active(), slug=slug).articles.published()
#     paginator = Paginator(article_list, 4)
#     page_obj = paginator.get_page(page)
#     data={
#         'Categories': get_object_or_404(Category, slug=slug, status=True),
#         'Articles': page_obj,
#     }
#     return render(request, 'news/category.html', context=data)

class CategoryList(ListView):
    template_name='news/category.html'
    paginate_by=4
    context_object_name='Articles'
    def get_queryset(self):
        global cat, slug
        slug=self.kwargs.get('slug')
        cat = get_object_or_404(Category, slug=slug, status=True)
        return cat.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Categories"] = cat
        return context


class AutherList(ListView):
    template_name='news/user.html'
    paginate_by=4
    context_object_name='Articles'
    def get_queryset(self):
        global author, username
        username=self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Author"] = author
        return context
    
