#Print how many rivers have at least one monitoring station AND print the first 10 of these rivers in alphabetical order

from geo import rivers_with_station,stations_by_river
from stationdata import build_station_list

stations = build_station_list()
rivers = rivers_with_station(stations)
print(len(rivers)," stations. First 10 -", sorted(rivers)[:10])

dic = stations_by_river(stations)
print(sorted(dic["River Aire"]))
print(sorted(dic["River Cam"]))
print(sorted(dic["River Thames"]))