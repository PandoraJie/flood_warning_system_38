#prints the name of 10 stations at which the current relative level is highest
#with relative level beside each station name

from stationdata import build_station_list, update_water_levels
from flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)
risk_stations = stations_highest_rel_level(stations,10)
for station in risk_stations:
    print(station.name,station.relative_water_level())