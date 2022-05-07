from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    department_id = models.OneToOneField('Department', on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=80)
    salary = models.IntegerField


class Realtor(Employee):
    district = models.CharField(max_length=200)
    clients_amount = models.IntegerField
    month_sold_buildings_amount = models.IntegerField


class Department(models.Model):
    dep_name = models.CharField(max_length=150)
    head_of_dep = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True)
    number_of_employees = models.IntegerField


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    passport_number_series = models.IntegerField


class Deal(models.Model):
    realtor = models.ForeignKey('Realtor', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)

    DEAL_STATUS = (
        ('A', 'Active'),
        ('C', 'Closed')
    )

    status = models.CharField(max_length=1, choices=DEAL_STATUS)

    class Meta:
        unique_together = ['realtor', 'client']