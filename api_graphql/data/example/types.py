from graphene.relay import Node
from graphene_django import DjangoObjectType

from example.models import Example

# Create your objects types here.


class ExampleNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Example
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'lastname': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
