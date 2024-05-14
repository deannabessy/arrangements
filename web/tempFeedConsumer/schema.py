import graphene

from graphene_django import DjangoObjectType, DjangoListField 
from .models import Reading 


class ReadingType(DjangoObjectType): 
    class Meta:
        model = Reading
        fields = "__all__"


class Query(graphene.ObjectType):
    all_readings = graphene.List(ReadingType)
    reading = graphene.Field(ReadingType, reading_id=graphene.Int())

    def resolve_all_readings(self, info, **kwargs):
        return Reading.objects.all()

    def resolve_reading(self, info, reading_id):
        return Reading.objects.get(pk=reading_id)

class ReadingInput(graphene.InputObjectType):
    id = graphene.ID()
    timestamp = graphene.DateTime()
    temp = graphene.Decimal()

class CreateReading(graphene.Mutation):
    class Arguments:
        reading_data = ReadingInput(required=True)

    reading = graphene.Field(ReadingType)

    @staticmethod
    def mutate(root, info, reading_data=None):
        reading_instance = Reading( 
            timestamp=reading_data.timestamp,
            temp=reading_data.temp
        )
        reading_instance.save()
        return CreateReading(reading=reading_instance)

class Mutation(graphene.ObjectType):
    create_reading= CreateReading.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)