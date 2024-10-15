from rest_framework.test import APITestCase
from django.urls import reverse


class LoginRequestTestCase(APITestCase):
    def test_login_request(self):
        url = reverse('login-request')
        data = {
            "phone_number": '+998975777467'
        }
        response = self.client.post(url, data, format='json')
        print(response.json())


__all__ = ['LoginRequestTestCase']
