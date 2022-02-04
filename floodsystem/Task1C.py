#Build a list of stations within 10 km of Cambridge

from geo import stations_within_radius
from stationdata import build_station_list

cam = (52.2053, 0.1218)
stations = build_station_list()
stations_10km = stations_within_radius(stations,cam,10)
names = []
for station in stations_10km:
    names.append(station.name)
print(sorted(names))