from graphene import String
from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from adoptions.models import Adoption

# Create your objects types here.


class AdoptionNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Adoption
        filter_fields = {
            'status': ['exact', 'icontains', 'istartswith'],
            'created_at': ['exact'],
            'update_at': ['exact'],
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
