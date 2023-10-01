from django.db import models as m
from django.urls import reverse


class Doctor(m.Model):
    firstname = m.CharField(max_length=40)
    lastname = m.CharField(max_length=40)
    expert = m.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Owner(m.Model):
    firstname = m.CharField(max_length=30)
    lastname = m.CharField(max_length=30)
    birthday = m.DateField()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Patient(m.Model):
    name = m.CharField(max_length=20)
    breed = m.CharField(max_length=20)
    age = m.IntegerField()
    owner = m.ForeignKey(Owner, on_delete=m.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info', args=[self.id])


class Status(m.Model):
    choise = (('VIP', 'vip'), ('Standart', 'standart'))
    name = m.CharField(max_length=30, choices=choise)

    def __str__(self):
        return self.name


class VetClinic(m.Model):
    title = m.CharField(max_length=30)
    doctor = m.ForeignKey(Doctor, on_delete=m.SET_NULL, null=True)
    rating = m.FloatField()
    patient = m.ForeignKey(Patient, on_delete=m.SET_NULL, null=True)
    owner = m.ForeignKey(Owner, on_delete=m.SET_NULL, null=True)
    summary = m.TextField(max_length=500)
    year = m.IntegerField()
    status = m.ForeignKey(Status, on_delete=m.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('info', args=[self.id])
