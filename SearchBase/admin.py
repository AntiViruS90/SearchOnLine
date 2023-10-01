from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Genre)  # Первый вариант
# admin.site.register(Director)
# admin.site.register(Actor)    # Первый вариант
# admin.site.register(Status)
admin.site.register(Country)
admin.site.register(AgeRating)
# admin.site.register(Film)


# for mod in models_list:       # Второй вариант
#     admin.site.register(mod)


class ActorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'birth_date')  # столбики в панеле админа
    list_display_links = ('firstname', 'lastname')  # имя и фамилия работают как ссылки


admin.site.register(Actor, ActorAdmin)  # Второй вариант || Регистрируем модель Актёр (class ActorAdmin)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')        # столбики в панеле админа
    list_display_links = ('firstname', 'lastname')  # имя и фамилия работают как ссылки


admin.site.register(Director, DirectorAdmin)


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'director', 'display_actors')
    list_filter = ('status', 'genre', 'rating')     # фильтр на странице создаётся автоматически
    # для поиска нужной информации
    fieldsets = (('О фильме', {'fields': ('title', 'actor', 'summary')}),
                 ('Рейтинг', {'fields': ('rating', 'ager', 'status')}),
                 ('Остальное', {'fields': ('genre', 'country', 'director', 'year')}))
    """ Здесь мы создаём секторы для внесения данных в таблицу
    О фильме:
            Название Актёры Описание
    Рейтинг:
            Рейтинг Возрастная категория Подписка
    Остальное:
            Жанр Страна Режиссёр Год
    """


admin.site.register(Film, FilmAdmin)


class StatusInLine(admin.TabularInline):
    """ TabularInline создаёт список из Film в линию
        StackedInline создаёт список из Film в столбик"""
    model = Film


class StatusAdmin(admin.ModelAdmin):
    inlines = [StatusInLine]    # inlines создаёт список, и в качестве
    # отображения на странице активирует class StatusInLine


admin.site.register(Status, StatusAdmin)
"""Здесь идёт перерегистрация из models.Status в данные из класса StatusAdmin
смотреть выше"""
