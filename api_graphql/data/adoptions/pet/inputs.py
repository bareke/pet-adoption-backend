from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Int
from graphene.types.scalars import Boolean

# Create your inputs types here.


class CreatePetInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de la mascota
    """

    name = String(required=True)
    type = String(required=True)
    age = Int(required=True)
    neutering = Boolean()
    breed = String()
    sex = String(required=True)


class UpdatePetInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización del ejemplo
    """

    id = ID(required=True)
    name = String()
    type = String()
    age = Int()
    neutering = Boolean()
    breed = String()
    sex = String()
