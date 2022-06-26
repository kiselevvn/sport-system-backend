from backend.apps.group_sportsmans.models import Group


def create_group_service(commit=True, **kwargs):
    """
    Сервис создания группы
    """

    group_instance = Group(**kwargs)

    if commit:
        group_instance.save()

    return group_instance
