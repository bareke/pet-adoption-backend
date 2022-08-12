from django.test import TestCase
from graphene import Schema

from adoptions.models import Pet
from api_graphql.schema import Query

# Create your tests here.


class PetTest(TestCase):

    def setUp(self) -> None:
        """Función que ejecuta la configuración inicial"""

        Pet.objects.create(
            name="salome",
            type="gato",
            age=7,
            neutering=True,
            breed="criollo",
            sex="h"
        )

        self.query_pet = """
            query qs {
                pet(id: "UGV0Tm9kZTox") {
                    name
                    type
                    age
                    neutering
                    breed
                    sex
                }
            }
        """

        self.query_all_pets = """
            query {
                allPets {
                    edges {
                        node {
                            name
                            type
                            age
                            neutering
                            breed
                            sex
                        }
                    }
                }
            }
        """

    def test_get_pet(self) -> None:
        """Prueba la consulta de obtener una mascota"""
        
        schema = Schema(query=Query)
        result = schema.execute(self.query_pet)

        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {
                "pet": {
                    "name": "salome",
                    "type": "gato",
                    "age": 7,
                    "neutering": True,
                    "breed": "criollo",
                    "sex": "h"
                }
            },
            result.data
        )

    def test_get_all_pets(self) -> None:
        """Prueba la consulta de obtener todas las mascotas"""

        schema = Schema(query=Query)
        result = schema.execute(self.query_all_pets)

        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {
                "allPets": {
                    "edges": [
                        {
                            "node": {
                                "name": "salome",
                                "type": "gato",
                                "age": 7,
                                "neutering": True,
                                "breed": "criollo",
                                "sex": "h"
                            }
                        }
                    ]
                }
            },
            result.data
        )
