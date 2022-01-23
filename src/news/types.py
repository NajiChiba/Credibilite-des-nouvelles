from graphene_mongo import MongoengineObjectType
from .models import New

class NewType(MongoengineObjectType):
    class Meta:
        model = New
