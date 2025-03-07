from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('view/all/', views.view_all, name='view-all'),
    path('update/', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
