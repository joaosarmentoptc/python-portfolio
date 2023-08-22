from django.urls import path
from .views import dashboard, create_employee, view_employee

app_name = 'employee'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create', create_employee, name='create_employee'),
    path('<uuid:uuid>', view_employee, name='view_employee'),
]