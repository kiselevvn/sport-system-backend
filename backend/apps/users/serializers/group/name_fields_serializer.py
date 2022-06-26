from rest_framework import serializers


class NameFieldsSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    second_name = serializers.CharField(max_length=250, required=False)
