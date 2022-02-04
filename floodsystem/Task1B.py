#Print a list of 10 closest and 10 furtherest stations from Cambridge


from geo import stations_by_distance
from stationdata import build_station_list

cam = (52.2053, 0.1218)
stations = build_station_list()
whole_list = stations_by_distance(stations,cam)
closest = whole_list[:10]
furtherest = whole_list[-10:]
print(closest)
print(furtherest)