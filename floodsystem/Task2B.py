#prints the name of each station at which the current relative level is over 0.8
#with the relative value alongside the name

from stationdata import build_station_list, update_water_levels
from flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)
list_over = stations_level_over_threshold(stations,0.8)
for tup in list_over:
    print(tup[0].name,tup[1])
#print(list_over)
#print(list_over[0][0].latest_level)
#print(list_over[0][0].typical_range)
#print(stations[0].relative_water_level())