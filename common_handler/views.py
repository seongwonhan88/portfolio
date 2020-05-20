from rest_framework.decorators import api_view
from rest_framework.response import Response

from .handlers.public_api import covid19_middleware_api


@api_view(['GET'])
def get_covid19_states(request, group):
    response = covid19_middleware_api(group)
    return_data = response.json()
    query = request.GET.get('state', None)
    if query:
        return_data = list(filter(lambda x: x['state'].lower() == query.lower(), return_data))
    return Response(return_data)


@api_view(['GET'])
def health_check(request):
    return Response({'status': 'healthy'})
