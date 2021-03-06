from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cat index'),
    path('cats/<int:cat_id>', views.cats_show, name='cats_show'),
    path('cats/create/', views.CatCreate.as_view(), name="cats_create" ),

]