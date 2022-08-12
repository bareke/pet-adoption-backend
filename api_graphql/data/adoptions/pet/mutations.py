from graphene import Mutation
from graphene import Field
from api_graphql.data.adoptions.pet.inputs import CreatePetInput, UpdatePetInput
from api_graphql.utils import delete_attributes_none, transform_global_ids

from adoptions.models import Pet
from api_graphql.data.adoptions.pet.types import PetNode


class CreatePet(Mutation):
    """Clase para crear mascotas"""

    pet = Field(PetNode)

    class Arguments:
        input = CreatePetInput(required=True)

    def mutate(self, info, input: CreatePetInput):
        input = delete_attributes_none(**vars(input))
        pet = Pet.objects.create(**input)

        return CreatePet(pet=pet)


class UpdatePet(Mutation):
    """Clase para actualizar mascotas"""

    pet = Field(PetNode)

    class Arguments:
        input = UpdatePetInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Pet.objects.filter(pk=input.get('id')).update(**input)
        pet = Pet.objects.get(pk=input.get('id'))
        pet.save()

        return UpdatePet(pet=pet)
