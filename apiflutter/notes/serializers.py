from rest_framework import serializers
from .models import Profession, Person

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'name']

class PersonSerializer(serializers.ModelSerializer):
    profession = serializers.StringRelatedField()

    class Meta:
        model = Person
        fields = ['id', 'name', 'age', 'cpf', 'data_nascimento', 'profession']


#Profession CRUD

def createProfession(self, validated_data):
    return Profession.objects.create(**validated_data)


def updateProfession(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)

#Person CRUD

def createPerson (self, validated_data):
    return Person.objects.create(**validated_data)

def updatePerson(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.age = validated_data.get('age', instance.age)
    instance.cpf = validated_data.get('cpf', instance.cpf)
    instance.data_nascimento = validated_data.get('data_nascimento', instance.data_nascimento)

    #foreign key
    profession_data = validated_data.get('fk_profession')
    if profession_data:
        instance.fk_profession = profession_data

    instance.save()
    return instance