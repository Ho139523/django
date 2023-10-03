from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .mixins import SuperseesMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from news.models import Articles

# Create your views here.
# @login_required
# def profile(request):
#     data={}
#     return render(request, 'registration/profile.html', context=data)

class Profile(LoginRequiredMixin, ListView):
    template_name='registration/profile.html'
    context_object_name='Articles'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Articles.objects.all()
        else:
            return Articles.objects.filter(writer=self.request.user)


class CreateArticle(LoginRequiredMixin, SuperseesMixin, CreateView):
    template_name='registration/article-create-update.html'
    model=Articles

