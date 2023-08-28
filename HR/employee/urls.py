from django.urls import path
from .views import dashboard, create_employee, view_employee, check_email_availability

app_name = 'employee'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create', create_employee, name='create_employee'),
    path('<uuid:uuid>', view_employee, name='view_employee'),
    path('check_email_availability', check_email_availability, name='check_email_availability'),
]