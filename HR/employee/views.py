import random

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

import core.enums
from employee.forms import EmployeeForm
from employee.models import Employee, Supervisor


# Create your views here.
def dashboard(request):
    employees = Employee.objects.all()
    employees_count = employees.count()
    employees_active_count = employees.filter(state='active').count()
    employees_leavers_count = employees.filter(state__in=['future_leaver','marked_as_leaver']).count()
    employees_approval_count = employees.filter(state__in=['draft']).count()

    paginator = Paginator(employees, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'employees': page_obj,
        'employees_count': employees_count,
        'employees_active_count': employees_active_count,
        'employees_leavers_count': employees_leavers_count,
        'employees_approval_count': employees_approval_count,
    }

    return render(request, 'index.html', context)


def create_employee(request):
    form = EmployeeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        try:
            employee = form.save()
            supervisor = Supervisor(
                supervisor_type=core.enums.SupervisorType.DIRECT,
                from_employee=Employee.objects.get(pk=request.POST['direct_manager']),
                to_employee=employee
            )
            supervisor.save()
        except:
            # TODO ERROR
            pass
        return redirect('employee:dashboard')

    context = {
        'form': form
    }
    return render(request, 'create_employee.html', context)


def view_employee(request,uuid):
    employee = Employee.objects.get(uuid=uuid)
    form = EmployeeForm(instance=employee, initial={'direct_manager': employee.get_supervisors_by_type('D')} or None)

    context = {
        'employee': employee,
        'form': form
    }
    return render(request, 'view_employee.html', context)