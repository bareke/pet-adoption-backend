from django.db.models import Model
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import IntegerField
from django.db.models import PositiveSmallIntegerField
from django.db.models import BooleanField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import ManyToManyField
from django.db.models import CASCADE

from .choices import SEX_CHOICES
from .choices import TYPE_CHOICES

# Create your models here.


class Client(Model):
    name = CharField(max_length=45, help_text='nombre')
    lastname = CharField(max_length=45, help_text='apellido')
    telephone = IntegerField(help_text='telefono')
    karma = IntegerField(help_text='karma')
    created_at = DateTimeField(
        auto_now_add=True,
        help_text='fecha de creación'
    )
    update_at = DateTimeField(
        auto_now=True,
        help_text='fecha de actualización'
    )

    def __str__(self) -> str:
        return f'{self.name} {self.lastname}'


class Pet(Model):
    name = CharField(max_length=25, help_text='nombre')
    type = CharField(max_length=25, choices=TYPE_CHOICES, help_text='tipo')
    age = PositiveSmallIntegerField(help_text='edad')
    neutering = BooleanField(
        null=True,
        blank=True,
        help_text='castración'
    )
    breed = CharField(
        max_length=25,
        null=True,
        blank=True,
        help_text='raza'
    )
    sex = CharField(max_length=1, choices=SEX_CHOICES, help_text='sexo')
    created_at = DateTimeField(
        auto_now_add=True,
        help_text='fecha de creación'
    )
    update_at = DateTimeField(
        auto_now=True,
        help_text='fecha de actualización'
    )

    # Relaciones
    # registers = ManyToManyField(
    #     Client,
    #     related_name='registers',
    #     through='Register',
    #     blank=True,
    #     help_text='registros'
    # )
    clients = ManyToManyField(
        Client,
        related_name='pets',
        through='Adoption',
        blank=True,
        help_text='adopciones'
    )

    def __str__(self) -> str:
        return self.name


class Vaccine(Model):
    name = CharField(max_length=45, help_text='nombre')
    datetime = DateTimeField(help_text='fecha')
    created_at = DateTimeField(
        auto_now_add=True,
        help_text='fecha de creación'
    )
    update_at = DateTimeField(
        auto_now=True,
        help_text='fecha de actualización'
    )

    # Relaciones
    pet = ForeignKey(Pet, related_name='vaccines', on_delete=CASCADE, help_text='mascota')

    def __str__(self) -> str:
        return self.name


# class Register(Model):
#     comment = TextField(help_text='comentario')
#     created_at = DateTimeField(
#         auto_now_add=True,
#         help_text='fecha de creación'
#     )
#     update_at = DateTimeField(
#         auto_now=True,
#         help_text='fecha de actualización'
#     )

#     # Relaciones
#     client = ForeignKey(
#         'Client',
#         related_name='registers',
#         on_delete=CASCADE,
#         help_text='cliente'
#     )
#     pet = ForeignKey(
#         'Pet',
#         related_name='registers',
#         on_delete=CASCADE,
#         help_text='mascota'
#     )

#     def __str__(self) -> str:
#         return self.comment


class Adoption(Model):
    status = CharField(max_length=10, help_text='estado')
    created_at = DateTimeField(
        auto_now_add=True,
        help_text='fecha de creación'
    )
    update_at = DateTimeField(
        auto_now=True,
        help_text='fecha de actualización'
    )

    # Relaciones
    client = ForeignKey(
        'Client',
        related_name='adoptions',
        on_delete=CASCADE,
        help_text='cliente'
    )
    pet = ForeignKey(
        'Pet',
        related_name='adoptions',
        on_delete=CASCADE,
        help_text='mascota'
    )

    def __str__(self) -> str:
        return self.status
