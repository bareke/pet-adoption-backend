from graphene import Schema

from api_graphql.schema import Mutation, Query

# Schema definition


schema = Schema(query=Query, mutation=Mutation)
