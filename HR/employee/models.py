from random import random

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from django_fsm import FSMField
import uuid
from core.enums import PersonalTitle, MaritalStatus, SupervisorType, Gender, UserStates, EmployeeType
from phonenumber_field.modelfields import PhoneNumberField

from core.models import Model


# Create your models here.
class Employee(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, null=False, editable=False)
    user_type = models.CharField(max_length=3, choices=EmployeeType.choices, default=EmployeeType.INTERNAL, blank=False)
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    personal_title = models.CharField(max_length=2, choices=PersonalTitle.choices, default=None, blank=True, null=True)
    date_of_birth = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=None, blank=True, null=True)
    nationality = CountryField(blank=False, default=None)
    disability = models.BooleanField(default=False, blank=False, null=False)
    marital_status = models.CharField(max_length=15, choices=MaritalStatus.choices, default=None, null=False)
    residential_country = CountryField(blank=False, default=None)
    residential_address = models.CharField(max_length=255, blank=False, null=False)
    residential_city = models.CharField(max_length=50, blank=False, null=False)
    residential_postal_code = models.CharField(max_length=10, blank=True, null=True)
    residential_phone = PhoneNumberField(blank=True, null=True)
    personal_email = models.EmailField(blank=False, null=False)
    employees_managed = models.ManyToManyField(
        'self',
        related_name='managers',
        symmetrical=False,
        through='Supervisor')
    state = FSMField(choices=UserStates.choices, default='draft', protected=True, null=False)

    def get_supervisors_by_type(self, type):
        return self.to_employee.filter(supervisor_type=type).first().from_employee

    def __str__(self):
        return f"""PW{self.user_id} : {self.user.first_name} {self.user.last_name}"""


class Supervisor(Model):
    from_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='from_employee')
    to_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='to_employee')
    supervisor_type = models.CharField(max_length=2, choices=SupervisorType.choices, default=None, blank=True)

    class Meta:
        unique_together = ['from_employee', 'to_employee']


@receiver(pre_save, sender=Employee)
def create_user(sender, instance, raw, **kwargs):
    user = User(email='test@jumia.com', first_name='hi', last_name='there', username=random(), is_active=0)
    user.save()
    instance.user_id = user.id
