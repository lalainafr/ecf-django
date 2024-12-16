from django.urls import path
from . import views
urlpatterns = [
    path('register-user/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    # activer le compte par mail
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('create-profile', views.create_profile, name='create_profile'),
    path('user-profile/<str:pk>', views.user_profile, name='user_profile'),
    path('edit-profile/<str:pk>', views.edit_profile, name='edit_profile'),
    path('list-profile', views.list_profile, name='list_profile'),
]