from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from Twitter_Api.get_jsons import get_json


def get_users_location(data: dict) -> list:
    """
    Get users' names and location from dictionary with information about these users.
    Return a list of users.

    >>> get_users_location(get_json("@BarackObama"))
    [['Bill Clinton', 'New York, NY'], ['Kamala Harris', 'California']]

    >>> get_users_location(get_json("@VasylLomachenko"))
    [['Eddie Hearn', 'Essex, UK'], ['Alexander Usyk', 'Украина'], ['NYPD 42nd Precinct', '830 Washington Ave., Bronx, NY']]
    """
    list_of_users_data = data["users"]
    list_of_users = [[element["name"], element["location"]] for element in list_of_users_data if
                     element["location"] != ""]

    return list_of_users


def add_users_coordinates(list_of_users: list) -> list:
    """
    Function find users' coordinates by their locations and
    add tuples with theses coordinates to the list with users' information.

    >>> add_users_coordinates(get_users_location(get_json("@BarackObama")))
    [['Bill Clinton', 'New York, NY', (40.7127281, -74.0060152)], ['Kamala Harris', 'California', (36.7014631, -118.755997)]]

    >>> add_users_coordinates(get_users_location(get_json("@VasylLomachenko")))
    [['Eddie Hearn', 'Essex, UK', (51.77046785, 0.46466977412300386)], ['Alexander Usyk', 'Украина', (49.4871968, 31.2718321)], ['NYPD 42nd Precinct', '830 Washington Ave., Bronx, NY', (40.8224393, -73.9113094)]]
    """
    for user in list_of_users:
        try:
            geolocator = Nominatim(user_agent="location_find")
            geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1, max_retries=1)
            location = geolocator.geocode(user[-1])
            user.append((location.latitude, location.longitude))
        except:
            continue

    return list_of_users
