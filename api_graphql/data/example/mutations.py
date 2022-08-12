from graphene import Mutation
from graphene import Field
from api_graphql.data.example.inputs import CreateExampleInput, UpdateExampleInput
from api_graphql.utils import delete_attributes_none, transform_global_ids

from example.models import Example
from api_graphql.data.example.types import ExampleNode


class CreateExample(Mutation):
    """Clase para crear ejemplos"""

    example = Field(ExampleNode)

    class Arguments:
        input = CreateExampleInput(required=True)

    def mutate(self, info, input: CreateExampleInput):
        input = delete_attributes_none(**vars(input))
        example = Example.objects.create(**input)

        return CreateExample(example=example)


class UpdateExample(Mutation):
    """Clase para actualizar ejemplos"""

    example = Field(ExampleNode)

    class Arguments:
        input = UpdateExampleInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Example.objects.filter(pk=input.get('id')).update(**input)
        example = Example.objects.get(pk=input.get('id'))

        return UpdateExample(example=example)
