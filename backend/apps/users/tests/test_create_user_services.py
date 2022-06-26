from django.test import TestCase
from django.contrib.auth import get_user_model
from ..services import (
    create_user_service,
    create_sportsman_service,
    create_employee_service,
)


class CreateUserServicesTestCase(TestCase):
    def setUp(self):
        self.user_info = {
            "username": "fakeusername",
            "email": "fake@fake.ru",
            "password": "fakepassword666",
        }
        self.sportsman_info = {
            "username": "fakesportsman",
            "email": "fakesportsman@fake.ru",
            "password": "fakesportsman66",
            "last_name": "ivanov",
            "first_name": "Ivan",
            "second_name": "Ivanovich",
        }
        self.employee_info = {
            "username": "fakeemployee",
            "email": "fakeemployee@fake.ru",
            "password": "fakeemployee66",
            "last_name": "ivanov",
            "first_name": "Ivan",
            "second_name": "Ivanovich",
            "is_examination_templates_manager": True,
            "is_staff": True,
        }

    def test_create_user_service(self):
        user_model = get_user_model()
        created_user = create_user_service(**self.user_info)
        username = self.user_info["username"]
        user = user_model.objects.get(username=username)
        self.assertEqual(user.password, created_user.password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.is_sportsman, False)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_examination_templates_manager, False)
        self.assertEqual(user.is_employee, False)

    def test_create_sportsman_service(self):
        user_model = get_user_model()
        created_sportsman = create_sportsman_service(**self.sportsman_info)
        username = self.sportsman_info["username"]
        sportsman = user_model.objects.get(username=username)
        self.assertEqual(sportsman.password, created_sportsman.password)
        self.assertEqual(sportsman.username, username)
        self.assertEqual(sportsman.is_sportsman, True)
        self.assertEqual(sportsman.is_staff, False)
        self.assertEqual(sportsman.is_examination_templates_manager, False)
        self.assertEqual(sportsman.is_employee, False)

    def test_create_employee_service(self):
        user_model = get_user_model()
        created_employee = create_employee_service(**self.employee_info)
        username = self.employee_info["username"]
        employee = user_model.objects.get(username=username)
        self.assertEqual(employee.password, created_employee.password)
        self.assertEqual(employee.username, username)
        self.assertEqual(employee.is_sportsman, False)
        self.assertEqual(employee.is_staff, True)
        self.assertEqual(employee.is_examination_templates_manager, True)
        self.assertEqual(employee.is_employee, True)
