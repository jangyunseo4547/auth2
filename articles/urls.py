from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
    # create
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/', views.detail, name = 'detail'),

    # comment_create 
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
    
    # comment_delete
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]