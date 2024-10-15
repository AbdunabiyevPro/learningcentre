from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginRequestTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(phone_number="+998905083995", is_verified=True)
        self.user2 = User.objects.create(phone_number="+998905083999", is_verified=True)

    def test_login_request(self):
        url = reverse('login-request')
        data = {
            "phone_number": "+998905083995"
        }
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response_data.get("success"))

    def test_more_attempts_to_login(self):
        url = reverse('login-request')
        data = {
            "phone_number": "+998905083999"
        }

        # First attempt should succeed
        response = self.client.post(url, data, format='json')
        response_data = response.json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response_data.get("success"))
        print("test_more_attempts_to_login", response_data)
        # Second attempt (immediately) should fail due to too many attempts
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print("test_more_attempts_to_login2", response_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response_data.get("success"))


all = ['LoginRequestTestCase']
