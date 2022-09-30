from rest_framework import serializers
from django.utils import timezone


class MeteringApiSerializer(serializers.Serializer):
    uniqueKey = serializers.CharField(max_length=256, required=True)
    customerId = serializers.CharField(max_length=256, required=True)
    clientId = serializers.CharField(max_length=256, required=True)
    timestamp = serializers.DateTimeField(required=False, default=timezone.now)
    bytes = serializers.IntegerField(required=True)
