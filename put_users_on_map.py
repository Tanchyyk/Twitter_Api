import folium
from folium.plugins import MarkerCluster


def put_users_on_map(list_of_users: list):
    """
    Function generates a map and put markers of users' locations on it.
    """
    users_map = folium.Map(tiles="Stamen Terrain", location=[49.8397, 24.0297], zoom_start=4)
    marker_cluster = folium.plugins.MarkerCluster().add_to(users_map)
    for user in list_of_users:
        folium.Marker(location=[user[-1][0], user[-1][1]],
                                          radius=10,
                                          popup=user[0],
                                          color='green',
                                          fill_opacity=0.5).add_to(marker_cluster)
    return users_map
