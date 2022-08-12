
from graphene import ObjectType
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

from .data.adoptions.adoption.types import AdoptionNode
from .data.adoptions.pet.mutations import CreatePet, UpdatePet
from .data.adoptions.pet.types import PetNode
from .data.adoptions.vaccine.types import VaccineNode
from .data.adoptions.client.types import ClientNode

# Schema definition


class Query(ObjectType):
    """Endpoint para consultar registros"""

    pet = Node.Field(PetNode)
    vaccine = Node.Field(VaccineNode)
    adoption = Node.Field(AdoptionNode)
    client = Node.Field(ClientNode)
    all_pets = DjangoFilterConnectionField(PetNode)
    all_vaccines = DjangoFilterConnectionField(VaccineNode)
    all_adoptions = DjangoFilterConnectionField(AdoptionNode)
    all_clients = DjangoFilterConnectionField(ClientNode)


class Mutation(ObjectType):
    """Endpoint para crear, actualizar y eliminar registros"""

    create_pet = CreatePet.Field()
    update_pet = UpdatePet.Field()
