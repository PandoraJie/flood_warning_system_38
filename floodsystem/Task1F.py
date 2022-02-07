from stationdata import build_station_list
from geo import inconsistent_typical_range_stations


stations = build_station_list()
name_list = []
for station in inconsistent_typical_range_stations(stations):
    name_list.append(station.name)
print(sorted(name_list))