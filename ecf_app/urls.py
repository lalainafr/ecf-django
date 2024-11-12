from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('competition/', views.competition, name='competition'),

    path('offer/', views.offer, name='offer'),
    path('data-save', views.data_save, name="data_save"),
    path('data-delete', views.data_delete, name="delete_data"),
    path('data-edit', views.data_edit, name="data_edit"),

]

