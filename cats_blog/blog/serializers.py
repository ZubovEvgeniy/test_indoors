from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Cat, User, CHOICES

import datetime as dt


class UserSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'cats',
        )


class CatSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    age = serializers.SerializerMethodField()
    color = serializers.ChoiceField(choices=CHOICES)

    class Meta:
        model = Cat
        fields = (
            'name',
            'color',
            'birth_year',
            'age',
            'breed',
            'owner',
        )
        read_only_fields = ('owner',)

        validators = [
            UniqueTogetherValidator(
                queryset=Cat.objects.all(),
                fields=('name', 'owner')
            )
        ]

    def get_age(self, obj):
        return dt.datetime.now().year - obj.birth_year

    def validate_birth_year(self, value):
        year = dt.date.today().year
        if not (year - 30 < value <= year):
            raise serializers.ValidationError('Проверьте год рождения')
        return value
