import json
import teslapy
from logs import logger


def tesla_get_location(request):
    with teslapy.Tesla('REMOVED') as tesla:
        vehicles = tesla.vehicle_list()
        vehicles[0].sync_wake_up()
        try:
            tesla_data = vehicles[0].api('VEHICLE_DATA')['response']['drive_state']
            lat = str(tesla_data['latitude'])
            lon = str(tesla_data['longitude'])
            if lat and lon:
                data = {'lat': lat, 'lon': lon, 'speed': tesla_data['speed']}
                json_data = json.dumps(data)
            else:
                raise ValueError("tesla_get_location::::: Either lat or lon is empty")
            return json_data
        except Exception as e:
            logger.error("tesla_get_location::::: Issue getting location::::: " + str(e))
            raise
