from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch


class CommunicationTests(APITestCase):

    def test_echo(self):
        with patch('CommunicationApp.views.CommunicationView.authenticate') as mocked_authenticate:
            mocked_authenticate.return_value.ok = True
            response = self.client.post("/api/echo/", {"message": "test message"}, format="json")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.json()["message"], "test message")

    def test_time(self):
        with patch('CommunicationApp.views.CommunicationView.authenticate') as mocked_authenticate:
            mocked_authenticate.return_value.ok = True
            response = self.client.get("/api/time/")
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertRegex(str(response.data), r'^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d*$')

