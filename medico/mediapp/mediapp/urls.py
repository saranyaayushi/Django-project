from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/',views.logoutuser, name='logout'),
    path('addmedicine/', views.add_medicine, name='add_medicine'),
    path('editmedicine/<int:medicine_id>/', views.edit_medicine, name='edit_medicine'),
    path('deletemedicine/<int:medicine_id>/', views.delete_medicine, name='delete_medicine'),
    path('', views.medicine_list, name='medicine_list'),
    path('searchmedicine/', views.search_medicine, name='search_medicine'),
]