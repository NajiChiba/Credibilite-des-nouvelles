import graphene
from django.core.exceptions import ObjectDoesNotExist
from graphene.types.scalars import ID
from mongoengine.signals import _FakeSignal
from .models import New
from .types import NewType


class NewInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    body = graphene.String()
    #fake = graphene.InputField()


class CreateNewMutation(graphene.Mutation):
    new = graphene.Field(NewType)

    class Arguments:
        new_data = NewInput(required=True)

    def mutate(self, info, new_data=None):
        new = New(
            title = new_data.title,
            body = new_data.body,
            #fake = new_data.fake
        )
        new.save()

        return CreateNewMutation(new=new)


'''

mutation creat{
  createNew(newData: {
    id: 2
    title: "New 2"
    body: "Body 2 Loreampson"
  }){
    new: new {
      id
    }
  }
}


'''



'''
class UpdateNewMutation(graphene.Mutation):
    New = graphene.Field(NewType)

    class Arguments:
        New_data = NewInput(required=True)

    @staticmethod
    def get_object(id):
        return New.objects.get(pk=id)

    def mutate(self, info, New_data=None):
        New = UpdateNewMutation.get_object(New_data.id)
        if New_data.name:
            New.name = New_data.name
        if New_data.brand:
            New.brand = New_data.brand
        if New_data.year:
            New.year = New_data.year
        if New_data.size:
            New.size = New_data.size
        if New_data.wheel_size:
            New.wheel_size = New_data.wheel_size
        if New_data.type:
            New.type = New_data.type

        New.save()

        return UpdateNewMutation(New=New)


class DeleteNewMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            New.objects.get(pk=id).delete()
            success = True
        except ObjectDoesNotExist:
            success = False

        return DeleteNewMutation(success=success)
'''