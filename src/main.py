import teslapy
import json
from config import settings


def tesla_get_location(request):
    """
    wrapper around the TeslaPy Python module that returns car's location in lat,lon format
    :param request: internal GCP Function param
    :return: location if available
    """
    with teslapy.Tesla(settings['production']['tesla']['username']) as tesla:
        wanted_key = 'drive_state'
        vehicles = tesla.vehicle_list()
        vehicles[0].sync_wake_up()
        tesla_data = vehicles[0].api('VEHICLE_DATA')
        if type(tesla_data) is not teslapy.JsonDict or wanted_key not in tesla_data['response']:
            return []
        else:
            drive_state = tesla_data['response'][wanted_key]
            lat = str(drive_state['latitude'])
            lon = str(drive_state['longitude'])
            data = {'lat': lat, 'lon': lon, 'speed': drive_state['speed']}
            return json.dumps(data)

#
# if __name__ == "__main__":
#     print(tesla_get_location(''))
