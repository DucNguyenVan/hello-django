from django.urls import path

from . import views 

app_name = 'project'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.detail, name="detail")
]