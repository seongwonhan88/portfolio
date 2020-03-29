import requests


def covid19_middleware_api(group=None):
    """
    This function works as a middleware. Django view handles detailed query params for detail search.
    https://docs.corona.lmao-xd.wtf/
    """
    base_api = 'https://corona.lmao.ninja'
    if not group:
        group = 'all'
    response = requests.get(f'{base_api}/{group}')
    return response
