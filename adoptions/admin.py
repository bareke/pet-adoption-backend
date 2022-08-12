from django.contrib import admin

from .models import Pet, Vaccine, Client, Adoption

# Register your models here.


@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'created_at',
        'update_at'
    )
    list_filter=('created_at','status',)
    search_fields=('created_at','status')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'lastname',
        'telephone',
        'karma',
        'created_at',
        'update_at'
    )
    list_filter=('created_at','karma',)
    search_fields=('created_at', 'name', 'lastname')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'age',
        'neutering',
        'breed',
        'sex',
        'created_at',
        'update_at'
    )
    list_filter=('created_at','type',)
    search_fields=('created_at','type')


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = (
        'pet',
        'name',
        'datetime',
        'created_at',
        'update_at'
    )
    list_filter=('name', 'datetime')
    list_filter=('name', 'datetime')
