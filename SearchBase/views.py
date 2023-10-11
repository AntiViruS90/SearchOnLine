from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, Group  # Создание юзера через программу
from .form import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

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

    if request.user.username:
        username = request.user.first_name
    else:
        username = 'Guest'
    # try:
    #     username = request.user.first_name
    # except:
    #     username = 'Guest'
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


def status(request):
    subscribe = Status.objects.all()
    data = {'subscribe': subscribe}
    return render(request, 'subscribe.html', data)
    pass


def prosmotr(request, id1, id2, id3):
    mas = ['FREE', 'BASE', 'VIP']  # film id2
    mas2 = ['VIP', 'BASE', 'FREE']  # user id3
    status = 0
    if id3 != 0:
        status = User.objects.get(id=id3)  # Нашли юзера
        status = status.groups.all()  # нашли его подписку
        status = status[0].id  # Нашли айди его подписки, она одна
        print(status)
    else:
        if id3 == 0:  # выдаёт гостю подписку номер 1 free
            status = 1
    if status >= id2:  # сравниваем статус и разрешение фильма
        print('ok')
        permission = True
    else:
        print('no')
        permission = False
    # return redirect('home')
    film = Film.objects.get(id=id1).title
    status = Group.objects.get(id=status).name
    status_film = Status.objects.get(id=id2).name
    data = {'film': film, 'status_film': status_film, 'status': status, 'permission': permission}
    return render(request, 'prosmotr.html', data)


def buy(request, type):
    user_id = request.user.id  # находим текущего юзера по номеру id
    user = User.objects.get(id=user_id)  # находим пользователя в таблице пользователей
    status_now = user.groups.all()[0].id  # нашли номер подписки в группе
    group_old = Group.objects.get(id=status_now)  # нашли подписку в таблице Group
    group_old.user_set.remove(user)  # При покупке новой подписки, нужно удалить старую подписку
    group_new = Group.objects.get(id=type)  # находим новую подписку из link, которую выбрал юзер
    group_new.user_set.add(user)  # добавляем юзера в таблицу с новой подпиской
    k1 = group_new.name
    data = {'subscribe': k1}
    return render(request, 'buy.html', data)


def subscribes(request):
    if request.user.username:
        username = request.user.first_name
    else:
        username = 'Guest'
    user_id = request.user.id  # находим текущего юзера по номеру id
    user = User.objects.get(id=user_id)  # находим пользователя в таблице пользователей
    status_now = user.groups.all()[0].id  # нашли номер подписки в группе
    status_name = Group.objects.get(id=status_now)
    subscribe = Group.objects.all()
    context = {'username': username, 'subscribe': subscribe, 'status_name': status_name}
    return render(request, 'subscribes.html', context)
    pass


def registration(request):
    # form = UserCreationForm()
    # встроенная функция Django from django.contrib.auth.forms import UserCreationForm
    if request.POST:
        form = SignUpForm(request.POST)     # а это наша созданная форма
        if form.is_valid():     # это проверка через python
            form.save()     # без .save() появляется ошибка в виде "__meta"
            username_from_form = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            first_name_from_form = form.cleaned_data.get('first_name')
            last_name_from_form = form.cleaned_data.get('last_name')
            email_from_form = form.cleaned_data.get('email')
            user = authenticate(username=username_from_form,
                                password=user_password)
            """Через команду authenticate мы сохраняем пользователя, но только имя и пароль, 
            так как authenticate это встроенная команда в Django 
            from django.contrib.auth import authenticate, login"""
            man = User.objects.get(username=username_from_form)
            # найдем нового пользователя и заполним поля в таблице
            man.email = email_from_form
            man.first_name = first_name_from_form
            man.last_name = last_name_from_form
            man.save()
            """Выше мы регистрируем данные пользователя в БД вручную, такие как:
            man.email = email_from_form
            man.first_name = first_name_from_form
            man.last_name = last_name_from_form
            man.save()"""
            login(request, user)    # с этим пользователем заходим на сайт
            user_group = Group.objects.get(id=1)
            user_group.user_set.add(man)
            """У таблицы Group и User есть связь, через add мы добавляем нового 
            пользователя в группу с бесплатной подпиской через
            user_group = Group.objects.get(id=1)"""
            return redirect('home')
            pass
    else:
        form = SignUpForm()
    data = {'registration_form': form}  # registration_form на странице HTML {{ registration_form }}
    return render(request, 'registration/registration.html', data)
