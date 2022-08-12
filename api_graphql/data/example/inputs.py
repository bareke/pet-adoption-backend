from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String

# Create your inputs types here.


class CreateExampleInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación del ejemplo
    """

    name = String(required=True)
    lastname = String(required=True)


class UpdateExampleInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización del ejemplo
    """

    id = ID(required=True)
    name = String()
    lastname = String()
