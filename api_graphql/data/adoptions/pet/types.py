from graphene import String
from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from adoptions.models import Pet

# Create your objects types here.


class PetNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    type = String()
    sex = String()

    class Meta:
        model = Pet
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'type': ['exact', 'icontains', 'istartswith'],
            'age': ['exact'],
            'neutering': ['exact'],
            'breed': ['exact', 'icontains', 'istartswith'],
            'sex': ['exact', 'icontains', 'istartswith'],
            'created_at': ['exact'],
            'update_at': ['exact'],
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
