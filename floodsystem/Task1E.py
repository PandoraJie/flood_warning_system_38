from stationdata import build_station_list
from geo import rivers_by_station_number


stations = build_station_list()
print(rivers_by_station_number(stations,9))