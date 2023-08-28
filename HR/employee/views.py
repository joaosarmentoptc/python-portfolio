from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

import core.enums
from employee.forms import EmployeeForm, UserForm
from employee.models import Employee, Supervisor


# Create your views here.
def dashboard(request):
    employees = Employee.objects.all()
    employees_count = employees.count()
    employees_active_count = employees.filter(state='active').count()
    employees_leavers_count = employees.filter(state__in=['future_leaver', 'marked_as_leaver']).count()
    employees_approval_count = employees.filter(state__in=['draft']).count()

    paginator = Paginator(employees, 5)
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
    employee_form = EmployeeForm(request.POST or None)
    user_form = UserForm(request.POST or None)
    if (request.method == 'POST'
            and employee_form.is_valid()
            and user_form.is_valid()):
        try:
            employee = employee_form.save(commit=False)
            employee.email = user_form.cleaned_data.get('email')
            employee.first_name = user_form.cleaned_data.get('first_name')
            employee.last_name = user_form.cleaned_data.get('last_name')
            employee.save()
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
        'employee_form': employee_form,
        'user_form': user_form
    }

    return render(request, 'create_employee.html', context)


def view_employee(request, uuid):
    employee = Employee.objects.get(uuid=uuid)
    form = EmployeeForm(instance=employee, initial={'direct_manager': employee.get_supervisors_by_type('D')} or None)

    context = {
        'employee': employee,
        'form': form
    }
    return render(request, 'view_employee.html', context)


def check_email_availability(request):
    first_name = request.GET['first_name']
    last_name = request.GET['last_name']

    email = first_name + '.' + last_name + '@company.com'

    email_is_not_available = User.objects.filter(email=email).first()

    if email_is_not_available:
        response_data = {'email': None}
    else:
        response_data = {'email': email}

    return JsonResponse(response_data)
