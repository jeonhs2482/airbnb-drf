from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from users.serializers import TinySerializer
from medias.serializers import PhotoSerializer
from categories.serializers import CategorySerializer

from .models import Perk, Experience


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceListSerializer(ModelSerializer):

    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "id",
            "country",
            "city",
            "name",
            "price",
            "rating",
            "is_host",
        )

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user


class ExperienceDetailSerializer(ModelSerializer):

    host = TinySerializer(
        read_only=True,
    )
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )
    category = CategorySerializer(
        read_only=True,
    )
    rating = serializers.SerializerMethodField()
    is_host = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = "__all__"

    def get_rating(self, experience):
        return experience.rating()

    def get_is_host(self, experience):
        request = self.context["request"]
        return experience.host == request.user
