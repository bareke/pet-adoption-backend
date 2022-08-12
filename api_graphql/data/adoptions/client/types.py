from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from adoptions.models import Client

# Create your objects types here.


class ClientNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Client
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'lastname': ['exact', 'icontains', 'istartswith'],
            'telephone': ['exact'],
            'karma': ['exact'],
            'created_at': ['exact'],
            'update_at': ['exact'],
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
