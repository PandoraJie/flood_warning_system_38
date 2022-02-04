from geo import stations_by_distance
from stationdata import build_station_list

#Print a list of 
cam = (52.2053, 0.1218)
stations = build_station_list()
result = stations_by_distance(stations,cam)[:10]
print(result)