from rest_framework import status
from rest_framework.test import APITestCase

from users.services import create_other_user, create_user


class UserAPITestCase(APITestCase):
    """Тестирование пользователей"""

    def setUp(self):
        """Установка данных"""

        self.user = create_user()
        self.other_user = create_other_user()

        response = self.client.post(
            "/api/users/login/", data={"email": "test.testov@mail.ru", "password": "123qwe456rty"}
        )

        response_for_other_owner = self.client.post(
            "/api/users/login/", data={"email": "ivan.ivanov@mail.ru", "password": "123qwe456rty"}
        )

        self.token = response.json()["access"]
        self.other_owner_token = response_for_other_owner.json()["access"]

        self.header = {"Authorization": f"Bearer {self.token}"}
        self.other_header = {"Authorization": f"Bearer {self.other_owner_token}"}

        self.car_data = {
            "brand": "Škoda",
            "model": "Octavia",
            "year": "2021",
            "fuel_type": "бензин",
            "transmission": "робот",
            "mileage": 12000,
            "price": 2800000,
            "owner_id": self.user.pk,
        }

        self.other_car_data = {
            "brand": "Volkswagen",
            "model": "Arteon Shooting Brake I",
            "year": "2020",
            "fuel_type": "дизель",
            "transmission": "робот",
            "mileage": 149000,
            "price": 3200000,
            "owner_id": self.other_user.pk,
        }

        self.patch_data = {"brand": "Volkswagen", "model": "Tiguan"}

    def test_car(self):
        """Тестирование CRUD машины"""

        response = self.client.post("/api/cars/", data=self.car_data, format="json", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post("/api/cars/", data=self.other_car_data, format="json", headers=self.other_header)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get("/api/cars/?brand=Volkswagen&mileage_min=10000", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        car_list = response.json()["results"]

        self.assertTrue(isinstance(car_list, list))

        self.assertEqual(len(car_list), 1)

        car_id = car_list[0]["id"]

        response = self.client.get(f"/api/cars/{car_id}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch(f"/api/cars/{car_id}/", data=self.patch_data, headers=self.other_header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.patch(f"/api/cars/{car_id}/", data=self.patch_data, headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(f"/api/cars/{car_id}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(f"/api/cars/{car_id}/", headers=self.other_header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
