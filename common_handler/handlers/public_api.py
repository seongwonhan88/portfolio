import requests


def covid19_middleware_api(group=None):
    base_api = 'https://corona.lmao.ninja'
    if not group:
        group = 'all'
    response = requests.get(f'{base_api}/{group}')
    return response
