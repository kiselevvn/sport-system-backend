from .create_user_service import create_user_service


def create_sportsman_service(commit=True, **kwargs):
    """Функция создания спортсмена

    last_name - имя

    first_name - фамилия

    second_name - отчество
    """
    user = create_user_service(commit=False, **kwargs)
    #
    user.last_name = kwargs["last_name"]
    user.first_name = kwargs["first_name"]
    user.second_name = kwargs["second_name"]
    user.birthday = kwargs["birthday"]
    #
    user.is_sportsman = True

    if commit:
        user.save()

    return user
