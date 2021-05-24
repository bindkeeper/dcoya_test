import unittest
from unittest.mock import patch
from client import Client


class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c = Client("localhost", "localhost")

    def test_api(self):
        with patch("client.requests.post") as mocked_post:
            mocked_post.return_value.status_code = 201
            mocked_post.return_value.json = unittest.mock.Mock(
                return_value="\"token\""
            )

            self.c.register("asd", "asd")
            self.assertEqual(self.c.jwt, "\"token\"")

        with patch("client.requests.post") as mocked_post:
            mocked_post.return_value.status_code = 200
            mocked_post.return_value.text = "message value"

            result = self.c._send_echo("message value")
            self.assertEqual(result, "message value")


if __name__ == '__main__':
    unittest.main()

