from django import forms
from django.contrib import admin
from base.models import Management, Sector, Department, Employee


class EmployeeAdminForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')

        if 'management' in self.data:
            management_id = self.data.get('management')
            self.fields['department'].queryset = Department.objects.filter(management_id=management_id)
        if 'department' in self.data:
            department_id = self.data.get('department')
            self.fields['sector'].queryset = Sector.objects.filter(department_id=department_id)

        if instance:
            if instance.department:
                self.fields['sector'].queryset = Sector.objects.filter(department_id=instance.department.id)


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeAdminForm
    list_display = ['name', 'management', 'department', 'sector']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['management'].queryset = Management.objects.all()
        form.base_fields['department'].queryset = Department.objects.none()
        form.base_fields['sector'].queryset = Sector.objects.none()
        return form


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Management)
admin.site.register(Department)
admin.site.register(Sector)
