from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from backend.apps.testing_sportsmans.models import TestTemplate


def get_test_template_mock(id: int):
    return {
        "name": f"string{id}",
        "description": f"string{id}",
        "slug": f"string{id}",
        "is_open": True,
        "is_published": True,
    }


class TestTemplatesViewsetTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("api/", include("apps.testing_sportsmans.api.urls")),
    ]

    def test_create(self):
        url = reverse("testing_sportsmans:test-template-list")
        response = self.client.post(
            url, get_test_template_mock(1), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list(self):
        for i in range(0, 5):
            t = TestTemplate(**get_test_template_mock(i))
            t.save()
        url = reverse("testing_sportsmans:test-template-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_detail(self):
        t = TestTemplate(**get_test_template_mock(1))
        t.save()
        url = reverse(
            "testing_sportsmans:test-template-detail", kwargs={"pk": t.pk}
        )
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch(self):
        t = TestTemplate(**get_test_template_mock(1))
        t.save()
        data = get_test_template_mock(2)
        url = reverse(
            "testing_sportsmans:test-template-detail", kwargs={"pk": t.pk}
        )
        response = self.client.patch(url, data, format="json")
        from django.forms.models import model_to_dict

        print(model_to_dict(t))
        print(data)
        # print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
