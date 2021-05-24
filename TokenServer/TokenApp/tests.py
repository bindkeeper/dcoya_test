from django.test import TestCase, Client

# Create your tests here.


class MYTestCase(TestCase):

    def test_user_list(self):
        client = Client()
        response = client.get('/api/show-client-list/')
        self.assertEqual(response.status_code, 200)

    def register(self):
        client = Client()
        response = client.post('/api/register-client/', {"username": "asdaa222", "password": "asd22"})
        print(f"data : {response.data}")
        self.jwt = response.data
        self.assertEqual(response.status_code, 201)

    def authentication_success(self):
        client = Client()
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + self.jwt,
        }
        print(f"auth_headers : {auth_headers}")
        response = client.get('/api/authorize-client/', **auth_headers)
        self.assertEqual(response.status_code, 200)

    def test_register_and_authentication(self):
        self.register()
        self.authentication_success()

    def test_failed_authentication(self):
        client = Client()
        response = client.get('/api/authorize-client/')
        self.assertNotEqual(response.status_code, 200)


