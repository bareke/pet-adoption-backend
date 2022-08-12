from django.contrib import admin
from .models import Example

# Register your models here.


@admin.register(Example)
class orderAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname')
    list_filter = ('name', 'lastname')
    search_fields = ('name', 'lastname')
