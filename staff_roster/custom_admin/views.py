from django.shortcuts import render, redirect
from django.http import JsonResponse
from base.models import Department, Sector
from .forms import EmployeeForm
from base.models import Management
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def employee_form(request):
    form = EmployeeForm()
    management_choices = Management.objects.all()  # Получение всех управлений
    return render(request, 'custom_admin/employee_form.html', {'form': form, 'management_choices': management_choices})


def get_departments(request):
    management_id = request.GET.get('management_id')
    departments = Department.objects.filter(management_id=management_id)
    data = [{'id': dep.id, 'name': dep.name} for dep in departments]
    print(departments)
    return JsonResponse(data, safe=False)


def get_sectors(request):
    department_id = request.GET.get('department_id')
    sectors = Sector.objects.filter(department_id=department_id)
    data = [{'id': sec.id, 'name': sec.name} for sec in sectors]
    return JsonResponse(data, safe=False)



@csrf_exempt
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Сотрудник успешно добавлен")
        else:
            messages.error(request, "Произошла ошибка при добавлении сотрудника")
        return redirect('employee_form')  # Перенаправляем на страницу с формой
    else:
        return JsonResponse({"error": "Недопустимый метод запроса"}, status=405)