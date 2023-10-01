from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Doctor)
admin.site.register(Owner)
# admin.site.register(Patient)
admin.site.register(Status)
# admin.site.register(VetClinic)


class AdminVetClinic(admin.ModelAdmin):
    list_display = ('title', 'rating', 'year')


admin.site.register(VetClinic, AdminVetClinic)


class AdminDoctor(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'expert')
    list_display_links = ('firstname', 'lastname')


admin.site.register(Doctor, AdminDoctor)


class AdminPatient(admin.ModelAdmin):
    list_display = ('breed', 'age', 'owner')


admin.site.register(Patient, AdminPatient)