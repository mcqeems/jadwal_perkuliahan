from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('logout/', views.logout_user, name='logout_user'),
    path('jadwal/', views.jadwal_kuliah, name='jadwal_kuliah'),
    path('dosen/', views.dosen, name='dosen'),
    path('jadwal/dosen/', views.jadwal_dosen, name='jadwal_dosen'),
    path('jadwal/dosen/edit/<int:id>/', views.edit_jadwal, name='edit_jadwal'),
]