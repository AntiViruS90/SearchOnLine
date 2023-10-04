"""
URL configuration for SearchOnLine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from SearchBase import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('film/', views.FilmsList.as_view(), name='allfilms'),
    # path('info/<int:id>/<str:title>', views.info, name='info')
    path('info/<slug:pk>/<str:title>', views.FilmDetailList.as_view(), name='info'),
    path('actor/', views.ActorList.as_view(), name='allactor'),
    path('actor_info/<slug:pk>', views.ActorDetailList.as_view(), name='actor_info'),
    path('director/', views.DirectorList.as_view(), name='alldirector'),
    path('director_info/<slug:pk>', views.DirectorDetailList.as_view(), name='director_info'),
    path('user/', include('django.contrib.auth.urls')),
    path('status/', views.status, name='status'),
    path('status/prosmotr/<int:id1>/<int:id2>/<int:id3>/', views.prosmotr, name='prosmotr')
]
"""
pk - Primary key identifying или айди(ID)
slug = Набор символов"""