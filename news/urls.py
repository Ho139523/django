from django.urls import path
from .views import Home, Description, CategoryList, AutherList


app_name='news'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('page/<int:page>', Home.as_view(), name='home'),
    path('article/<slug:slug>/', Description.as_view(), name='description'),
    path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name='category'),
    path('author/<slug:username>/', AutherList.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>', AutherList.as_view(), name='author'),
]


