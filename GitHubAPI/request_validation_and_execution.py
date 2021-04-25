import requests
from .constants import StatusCode
from django.conf import settings


def page_parameter_given(request):
    return 'page' in request.GET


def user_parameter_given(request):
    return 'user' in request.GET


def build_api_url(request):
    user = request.GET['user']
    url = 'https://api.github.com/users/{}/repos?per_page=4'.format(user)
    if page_parameter_given(request):
        url += '&page=' + request.GET['page']

    return url


def build_header():
    if settings.GITHUB_TOKEN is not None:
        return {'Authorization': 'token %s' % settings.GITHUB_TOKEN}
    return {}


def build_result(request, url, header):
    result = []
    next_page = True
    while next_page:
        response = requests.get(url, headers=header)
        status_code = response.status_code

        if status_code != StatusCode.OK:
            return None, status_code

        result.extend(response.json())

        if page_parameter_given(request):
            return result, status_code

        next_page = 'next' in response.links
        if next_page:
            url = response.links['next']['url']

    return result, status_code


def request_validation_and_execution(view):
    def wrapper(request):

        if not user_parameter_given(request):
            return view(request, response={'response': 'User parameter has not been provided'}, status_code=StatusCode.BAD_REQUEST)

        header = build_header()
        url = build_api_url(request)
        result, status_code = build_result(request, url, header)

        if status_code == StatusCode.OK:
            return view(request, response=result, status_code=status_code)

        return view(request, response={'response': 'GitHub API responded with error'}, status_code=status_code)

    return wrapper