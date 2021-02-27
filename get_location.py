from geopy import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def get_users_location(data) -> list:
    list_of_users_data = data["users"]
    list_of_users = [[element["name"], element["location"]] for element in list_of_users_data if element["location"] != ""]

    return list_of_users


def add_users_coordinates(list_of_users: list) -> list:
    for user in list_of_users:
        try:
            geolocator = Nominatim(user_agent="location_find")
            geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1, max_retries=1)
            location = geolocator.geocode(user[-1])
            user.append((location.latitude, location.longitude))
        except:
            continue

    return list_of_users
