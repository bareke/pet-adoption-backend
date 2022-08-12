from django.db.models import Model
from django.db.models import CharField
from django.db.models import DateTimeField

# Create your models here.


class Example(Model):
    name = CharField(max_length=45)
    lastname = CharField(max_length=45)
    created_at = DateTimeField(
        auto_now_add=True,
        help_text='fecha de creación'
    )
    updated_at = DateTimeField(
        auto_now=True,
        help_text='fecha de actualización'
    )


    def __str__(self) -> str:
        return f'{self.name} {self.lastname}'
