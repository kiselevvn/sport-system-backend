from rest_framework import serializers


class AccountFieldsSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    password2 = serializers.CharField(max_length=30)

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Введённые пароли не совпадают")
        return data

    def validate_password(self, value):
        if value == "":
            raise serializers.ValidationError(
                "Пустая строка не может являться паролем"
            )
        return value

    # def validate_username(self, value):
    #     raise serializers.ValidationError("error string")
    #     return value