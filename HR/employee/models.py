import uuid
from random import random

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django_countries.fields import CountryField
from django_fsm import FSMField
from phonenumber_field.modelfields import PhoneNumberField

from core.enums import PersonalTitle, MaritalStatus, SupervisorType, Gender, UserStates, EmployeeType, Company, \
    ProbationPeriod, NetOrGross
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
        return getattr(self.to_employee.filter(supervisor_type=type).first(), 'from_employee', None)

    def __str__(self):
        return f"""PW{self.user_id} : {self.user.first_name} {self.user.last_name}"""


class Supervisor(Model):
    from_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='from_employee')
    to_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='to_employee')
    supervisor_type = models.CharField(max_length=2, choices=SupervisorType.choices, default=None, blank=True)

    class Meta:
        unique_together = ['from_employee', 'to_employee']


class ContractCategory(Model):
    contract_category = models.CharField(max_length=10)


class ContractType(Model):
    contract_type = models.CharField(max_length=10)
    contract_category = models.ForeignKey(ContractCategory, on_delete=models.DO_NOTHING)


class LegalEntity(Model):
    legal_entity = models.CharField(max_length=10)
    country = CountryField(blank=False, null=False)


class Contract(Model):
    city = models.CharField(max_length=25, blank=False, null=False)
    company = models.CharField(max_length=10, choices=Company.choices, default=Company.JUMIA, blank=False)
    contract_type = models.ForeignKey(ContractType, on_delete=models.DO_NOTHING)
    legal_entity = models.ForeignKey(LegalEntity, on_delete=models.DO_NOTHING)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)
    probation_period = models.CharField(
        max_length=10,
        choices=ProbationPeriod.choices,
        default=ProbationPeriod._NA,
        blank=False,
        null=False)


class Salary(Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    annual_basic_salary = models.PositiveIntegerField(blank=False, null=False)
    currency_code = models.CharField(max_length=10, blank=False, null=False)
    effective_date = models.DateField(blank=False, null=False)


class Entitlements(Model):
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(blank=False, null=False)
    include_in_salary = models.BooleanField(default=False, blank=False, null=False)
    net_or_gross = models.CharField(max_length=1, choices=NetOrGross.choices, blank=False, null=False)


@receiver(pre_save, sender=Employee)
def create_user(sender, instance, raw, **kwargs):
    user = User(email='test@jumia.com', first_name='hi', last_name='there', username=random(), is_active=0)
    user.save()
    instance.user_id = user.id
