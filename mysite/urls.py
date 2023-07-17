from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:content_id>/', views.detail, name='detail'),
    path('comment/create/<int:content_id>/', views.comment_create, name='comment_create'),
]
