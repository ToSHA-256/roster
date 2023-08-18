from django.shortcuts import render
from django.http import JsonResponse
from base.models import Department, Sector
from .forms import EmployeeForm
from base.models import Management


def employee_form(request):
    form = EmployeeForm()
    management_choices = Management.objects.all()  # Получение всех управлений
    return render(request, 'custom_admin/employee_form.html', {'form': form, 'management_choices': management_choices})



def get_departments(request):
    management_id = request.GET.get('management_id')
    departments = Department.objects.filter(management_id=management_id)
    data = [{'id': dep.id, 'name': dep.name} for dep in departments]
    return JsonResponse(data, safe=False)


def get_sectors(request):
    department_id = request.GET.get('department_id')
    sectors = Sector.objects.filter(department_id=department_id)
    data = [{'id': sec.id, 'name': sec.name} for sec in sectors]
    return JsonResponse(data, safe=False)
