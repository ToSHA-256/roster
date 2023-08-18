from django.db import models


class Management(models.Model):
    name = models.CharField(max_length=100)


class Department(models.Model):
    name = models.CharField(max_length=100)
    management = models.ForeignKey(Management, on_delete=models.CASCADE)


class Sector(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


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
