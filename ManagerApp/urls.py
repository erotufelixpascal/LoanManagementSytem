from django.urls import path
from ManagerApp import views

app_name = 'managerApp'

urlpatterns = [
    path('admin-login/', views.superuser_login_view, name='admin-login'),
    path('dashboard/', views.dashboard, name ='dashboard')
    path()
]

