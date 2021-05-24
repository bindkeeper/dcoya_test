import requests
import argparse
import logging

logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s', level=logging.INFO)


class Client:
    def __init__(self, token_server, communication_server):
        self.token_server = token_server
        self.communication_server = communication_server
        self.jwt = None
        self.commands = {"echo": self._perform_echo, "time": self._perform_time}

    def get_possible_commands(self):
        return list(self.commands.keys())

    def register(self, user_name, password):
        r = requests.post(f"http://{self.token_server}:8080/api/register-client/",
                          json={"username": user_name, "password": password})
        logging.info(f"received jwt : {r.json()}")
        if r.status_code == 201:
            self.jwt = r.json()
        else:
            raise RuntimeError("Failed to authenticate")

    def perform_command(self, command):
        try:
            self.commands[command]()
        except KeyError:
            logging.info(f"no such command {command}")

    def _perform_echo(self):
        logging.info(f"echo entered")
        message = input("please enter the message:\n")
        print(self._send_echo(message))

    def _send_echo(self, message):
        if not self.jwt:
            raise RuntimeError("no JWT token")

        r = requests.post(f'http://{self.communication_server}/api/echo/',
                         headers={'AUTHORIZATION': 'Bearer ' + self.jwt},
                         json={"message": message})

        print(r.status_code)
        return r.text

    def _perform_time(self):
        logging.info(f"time entered")
        print(self._send_time())

    def _send_time(self):
        if not self.jwt:
            raise RuntimeError("no JWT token")

        r = requests.get(f'http://{self.communication_server}/api/time/',
                         headers={'AUTHORIZATION': 'Bearer ' + self.jwt})
        return r.text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token_server', required=True, help='Token Server address')
    parser.add_argument('--communication_server', required=True, help='Communication Server address')
    parser.add_argument('--username', required=True, help='User name')
    parser.add_argument('--password', required=True, help='Password')
    args = parser.parse_args()

    c = Client(args.token_server, args.communication_server)
    try:
        c.register(args.username, args.password)
        possible_commands = ", ".join(c.get_possible_commands())
        print(f"possible commands are: \n{possible_commands}\nenter \"exit\" to exit the app")
        while True:
            command = input(f"\nnext command please:\n")
            if command == "exit":
                break
            c.perform_command(command)

    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()
