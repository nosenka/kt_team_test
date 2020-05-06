from rest_framework import serializers
from . import models


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Rate
        fields = ("id", "source_currency", "dest_currency", "price", "rate_updated_at", "created_at")
