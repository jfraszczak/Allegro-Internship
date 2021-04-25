from rest_framework.decorators import api_view
from rest_framework.response import Response
from .constants import StatusCode, FieldName
from .request_validation_and_execution import request_validation_and_execution


@api_view(['GET'])
@request_validation_and_execution
def repositories_list(request, status_code=None, response=None):
    if status_code != StatusCode.OK:
        return Response(response, status=status_code)

    listed_repositories = []
    for repository_data in response:
        listed_repositories.append({
            'name': repository_data[FieldName.name_field],
            'stars_count': repository_data[FieldName.stars_count_field]
        })

    return Response(listed_repositories, status=status_code)


@api_view(['GET'])
@request_validation_and_execution
def stars_count_sum(request, status_code=None, response=None):
    if status_code != StatusCode.OK:
        return Response(response, status=status_code)

    stars_sum = sum([repository_data[FieldName.stars_count_field] for repository_data in response])

    return Response({'stars_count_sum': stars_sum}, status=status_code)
