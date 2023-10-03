from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User  # Создание юзера через программу


# Create your views here.


def index(request):
    sum_film = Film.objects.all().count()
    # здесь он получает данные из БД Film и выводит сумму при помощи count()
    sum_actor = Actor.objects.all().count()
    # здесь он получает данные из БД Actor и выводит сумму при помощи count()
    sum_status = Film.objects.filter(status__film=2).count()
    """При помощи фильтра получает значение подписки, которое привязано к Film в БД
    filter(status__film=2) т.к. только Film может получать данные из Status, то здесь
    через двойное подчёркивание (__) status получает данные из film
    """
    try:
        username = request.user.first_name
    except:
        username = 'Guest'
    context = {'film': sum_film, 'actor': sum_actor, 'status': sum_status, 'username': username}
    # user = User.objects.create_user('Petr', 'petr@example.com', 'PetrPetr')
    # user.first_name = 'Petr'
    # user.last_name = 'Petrov'
    # user.save()
    """
    Выше мы создали юзера вручную через
    from django.contrib.auth.models import User
    """
    return render(request, 'index.html', context=context)


# def allfilms(request):
#     return render(request, 'index.html') можно сделать так
from django.views import generic  # generic генерирует что-то


class FilmsList(generic.ListView):
    model = Film
    paginate_by = 2


# from django.http import HttpResponse


# def info(request, id):  # Первый вариант
#     id = int(id)
#     film = Film.objects.get(id=id)
#     return HttpResponse(film.title)


class FilmDetailList(generic.DetailView):  # Второй вариант
    model = Film


"""
В модуле DetailView нужно применять функцию get_absolute_url,
который был включен в файле models.Film => def 
get_absolute_url(self):
    return reverse([путь] = 'info' (который в url.py), ([аргумент, 
    что именно нужно конвертировать]) args=[self.id])

"""


class ActorList(generic.ListView):
    model = Actor


class ActorDetailList(generic.DetailView):
    model = Actor


class DirectorList(generic.ListView):
    model = Director


class DirectorDetailList(generic.DetailView):
    model = Director