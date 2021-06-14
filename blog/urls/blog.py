from django.urls import path

from ..views import blogs

urlpatterns_blog = [
    path('', blogs.index, name='blog_index'),
    path('<int:pk>/', blogs.detail, name='blog_detail'),
    path('<category_name>/', blogs.category, name='blog_category')
]