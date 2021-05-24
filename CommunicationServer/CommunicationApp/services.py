import requests


def check_authentication(jwt):
    if not jwt:
        return False

    r = requests.get('http://localhost:8080/api/authorize-client/',
                     headers={'AUTHORIZATION': 'Bearer ' + jwt})
    if r.status_code == 200:
        return True
    else:
        return False
