from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # offer
    path('offer/', views.offer, name='offer'),
    path('data-save', views.data_save, name="data_save"),
    path('data-delete', views.data_delete, name="delete_data"),
    path('data-edit', views.data_edit, name="data_edit"),

    # competition
    path('create-competition/', views.create_competition, name='create_competition'),
    path('detail-competition/<str:pk>', views.detail_competition, name='detail_competition'),
    path('list-competition/', views.list_competition, name='list_competition'),
    path('edit-competition/<str:pk>', views.edit_competition, name='edit_competition'),
    path('delete-competition/<str:pk>', views.delete_competition, name='delete_competition'),
]

