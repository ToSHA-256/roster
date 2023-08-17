from django.db import models


class Management(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} управление'

    class Meta:
        verbose_name = 'Управление'
        verbose_name_plural = 'Управления'


class Department(models.Model):
    name = models.CharField(max_length=100)
    management = models.ForeignKey(Management, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} отдел {self.management}'

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Sector(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} сектор {self.department}'

    class Meta:
        verbose_name = 'Сектор'
        verbose_name_plural = 'Сектора'


class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    STATUS_CHOICES = [
        ('military', 'Военнослужащий'),
        ('civil', 'Госслужащий'),
    ]
    surname = models.CharField(max_length=100,default=None)
    name = models.CharField(max_length=100,default=None)
    patronymic = models.CharField(max_length=100,default=None)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES,default='military')
    date_of_birth = models.DateField(default='2000-01-01')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees',default=None)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='employees',default=None)
    management = models.ForeignKey(Management, on_delete=models.CASCADE, related_name='employees',default=None)

    def __str__(self):
        initials = f'{self.surname} {self.name[0]}.{self.patronymic[0]}.'
        return initials
