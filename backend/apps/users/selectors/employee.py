from backend.apps.users.models import Employee


def get_employees():
    return Employee.objects.all()
