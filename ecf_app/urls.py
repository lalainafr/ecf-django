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
    
    # cart
    path('detail-competition/competition/<str:pk>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    
    path('cart', views.cart, name='cart'),
    
    path('remove-from-cart/<str:pk>', views.remove_from_cart, name='remove_from_cart'),
    
    path('invoice', views.invoice, name='invoice'),
    path('payment', views.payment, name='payment'),
    path('valid-payment', views.valid_payment, name='valid_payment'),
    path('payment-list/<str:user>', views.payment_list, name='payment_list'),
    
    path('check-ticket/<str:userUid>/<str:paymentUid>', views.check_ticket, name='check_ticket'),
    path('ticket-list/<str:user>', views.ticket_list, name='ticket_list'),
    path('ticket-detail/<int:pk>', views.ticket_detail, name='ticket_detail'),

    path('all-ticket-list', views.all_ticket_list, name='all_ticket_list'),
]

