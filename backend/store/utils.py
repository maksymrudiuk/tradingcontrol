from geopy.geocoders import Nominatim


def get_location(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address, timeout=20)
    return (location.latitude, location.longitude)


def get_address(coords):
    geolocator = Nominatim()
    location = geolocator.reverse(coords, timeout=20)
    return (location.address)
