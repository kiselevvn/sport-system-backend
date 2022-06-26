from rest_framework import serializers


class EmployeeStatusesSerializer(serializers.Serializer):
    is_examination_templates_manager = serializers.BooleanField()
    is_staff = serializers.BooleanField()
