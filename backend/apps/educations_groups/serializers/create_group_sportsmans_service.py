from ..models import Group


def create_group_sportsmans_service(commit=True, **kwargs: dict) -> Group:
    """Сервис создания группы спортсменов"""
    group_instance = Group(**kwargs)

    if commit:
        group_instance.save()

    return group_instance
