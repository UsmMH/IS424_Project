from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list_view, name='class_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('classes/', views.class_list_view, name='class_list'),
    path('classes/add/', views.class_add_view, name='class_add'),
    path('classes/<int:pk>/', views.class_detail_view, name='class_detail'),
    path('classes/<int:pk>/update/', views.class_update_view, name='class_update'),
    path('my-bookings/', views.my_bookings_view, name='my_bookings'),
]
