from rest_framework.decorators import api_view
from rest_framework.response import Response

from common_handler.handlers.public_api import covid19_middleware_api


@api_view(['GET'])
def get_covid19_status(request):
    query = request.GET.get('state', None)
    response = covid19_middleware_api('states')
    return_data = response.json()
    if query:
        return_data = list(filter(lambda x: x['state'].lower() == query.lower(), return_data))
    return Response(return_data)
