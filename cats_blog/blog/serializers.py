from rest_framework import serializers

from .models import Cat, Owner, CHOICES

import datetime as dt


class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = (
            'first_name',
            'last_name',
            'cats',
        )


class CatSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    age = serializers.SerializerMethodField()
    color = serializers.ChoiceField(choices=CHOICES)

    class Meta:
        model = Cat
        fields = (
            'name',
            'color',
            'age',
            'breed',
            'owner',
        )

    def get_age(self, obj):
        return dt.datetime.now().year - obj.birth_year
