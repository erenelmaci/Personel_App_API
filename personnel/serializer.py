from rest_framework import serializers
from .models import (
    Personnel, Department
)


class PersonnelSerializers(serializers.ModelSerializer):

    class Meta:
        model = Personnel
        fields = ('first_name',
                  'last_name',
                  'title')


class DepartmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentPersonelSerializers(serializers.ModelSerializer):

    personnel = PersonnelSerializers(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'personnel')
