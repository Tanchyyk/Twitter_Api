import requests


def get_json(user_name):
    """
    Function sent request to Twitter Api and  get .json object with information about current twitter user.
    """
    base_url = "https://api.twitter.com/1.1/friends/list.json"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAKkSNAEAAAAADGjajQeyVyQTi28qCAff1Mrl520%3DGzjvYM2YJgXGIMZQzXE23E4jUcSmIsOpsGCQcAnhL87so6O4JC"

    search_headers = {
        "Authorization": f'Bearer {bearer_token}'
    }
    search_params = {
        "screen_name": user_name,
        "count": 4
    }

    response = requests.get(base_url, headers=search_headers, params=search_params)
    return response.json()
