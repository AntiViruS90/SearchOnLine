from django.db import models as m
from django.urls import reverse


class Genre(m.Model):
    name = m.CharField(max_length=30, verbose_name='Жанр')  # verbose_name - отображение данных в таблице АДМИНа

    def __str__(self):
        return self.name


class Director(m.Model):
    firstname = m.CharField(max_length=30)  # verbose_name - отображение данных в таблице АДМИНа
    lastname = m.CharField(max_length=30)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def get_absolute_url(self):
        return reverse('director_info', args=[self.id])


class Actor(m.Model):
    firstname = m.CharField(max_length=30)
    lastname = m.CharField(max_length=30)
    birth_date = m.DateField(blank=True, null=True)
    country = m.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def get_absolute_url(self):
        return reverse('actor_info', args=[self.id])


class Status(m.Model):
    CHOICE = (('FREE', 'free'), ('BASE', 'base'), ('VIP', 'vip'))
    name = m.CharField(max_length=30, choices=CHOICE)

    def __str__(self):
        return self.name


class Country(m.Model):
    name = m.CharField(max_length=30)

    def __str__(self):
        return self.name


class AgeRating(m.Model):
    choice = (('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'))
    rate = m.CharField(max_length=5, choices=choice)

    def __str__(self):
        return self.rate


class Film(m.Model):
    title = m.CharField(max_length=30)
    genre = m.ForeignKey(Genre, on_delete=m.SET_DEFAULT, default=1)
    rating = m.FloatField()
    country = m.ForeignKey(Country, on_delete=m.SET_NULL, null=True)
    director = m.ForeignKey(Director, on_delete=m.SET_NULL, null=True)
    summary = m.TextField(max_length=500)
    year = m.IntegerField()
    ager = m.ForeignKey(AgeRating, on_delete=m.SET_NULL, null=True)
    actor = m.ManyToManyField(Actor)
    status = m.ForeignKey(Status, on_delete=m.SET_DEFAULT, default=1)

    def __str__(self):
        return self.title

    def display_actors(self):
        res = ''
        for actor in self.actor.all():  # Создаём функцию для вывода имён в таблице admin
            """Из списка всех актёров через цикл выдаёт весь список актёров.
            К переменной res мы прибавляем имя актёра, [пробел], и фамилию актёра"""
            res += actor.firstname + ' ' + actor.lastname + ' '
        return res
    display_actors.short_description = 'Actors'

    def get_absolute_url(self):
        return reverse('info', args=[self.id, self.title])
        # return f'kino/{self.id}/{self.title}'


models_list = [Genre, Director, Actor, Status, Country, AgeRating, Film]