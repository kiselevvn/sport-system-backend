from ..models import Group


def bulk_create_group_sportsmans_service(
    groups: list,
    commit=True,
) -> list:
    """Сервис создания группы спортсменов"""
    list_group_instance = []

    for group in groups:
        list_group_instance.append(Group(**group))

    if commit:
        Group.objects.bulk_create(list_group_instance)

    return list_group_instance
