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
    name = models.CharField(max_length=100)
    management = models.ForeignKey(
        Management,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    sector = models.ForeignKey(
        Sector,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
