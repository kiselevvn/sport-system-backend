from django.contrib.auth import get_user_model


def create_user_service(commit=True, **kwargs):
    """
    Функция создания пользователя системы

    username - логин

    email - электронная почта

    password - пароль
    """
    user_model = get_user_model()
    user = user_model.objects.create_user(
        kwargs["username"], kwargs["email"], kwargs["password"]
    )
    #

    if commit:
        user.save()

    return user
