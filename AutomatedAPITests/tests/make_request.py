import requests


def make_request(path_parameter=None):
    base_url = 'https://api.rawg.io/api/games/elden-ring'
    if path_parameter:
        url = f'{base_url}/{path_parameter}'
    else:
        url = base_url
    url = f'{url}?key=API_KEY'
    response = requests.get(url)
    return response
