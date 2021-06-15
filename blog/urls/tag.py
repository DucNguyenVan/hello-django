from django.urls import path

from ..views import tags

urlpatterns_tag = [
    path('tag/', tags.index, name='tag_index'),
    path('tag/<int:pk>/', tags.detail, name='tag_detail'),
    path('tag/create/', tags.create_tag, name='tag_create')
]