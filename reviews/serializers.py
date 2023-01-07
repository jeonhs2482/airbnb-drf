from rest_framework import serializers

from users.serializers import TinySerializer

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = TinySerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            "user",
            "payload",
            "rating",
        )
