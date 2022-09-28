import json
import teslapy


def tesla_get_location(request):
    with teslapy.Tesla('REMOVED') as tesla:
        vehicles = tesla.vehicle_list()
        vehicles[0].sync_wake_up()
        tesla_data = vehicles[0].api('VEHICLE_DATA')['response']['drive_state']
        lat = str(tesla_data['latitude'])
        lon = str(tesla_data['longitude'])
        data = {'lat': lat, 'lon': lon, 'speed': tesla_data['speed']}
        json_data = json.dumps(data)
    return json_data
    #return str(tuple_latlon)
