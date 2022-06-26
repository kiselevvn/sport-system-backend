from .create_user_service import create_user_service


def create_employee_service(commit=True, **kwargs):
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
    #
    user.is_employee = True
    #
    if kwargs["is_examination_templates_manager"]:
        user.is_examination_templates_manager = kwargs[
            "is_examination_templates_manager"
        ]
    if kwargs["is_staff"]:
        user.is_staff = kwargs["is_staff"]

    if commit:
        user.save()

    return user
