import graphene
from .models import New
from .types import NewType
from .mutations import CreateNewMutation

class Mutations(graphene.ObjectType):
    create_new = CreateNewMutation.Field()


class Query(graphene.ObjectType):
    
    all_news = graphene.List(NewType)

    def resolve_all_news(self, info):
        return New.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutations, types=[NewType])

