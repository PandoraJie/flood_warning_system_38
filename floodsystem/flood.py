
from stationdata import build_station_list, update_water_levels
from utils import sorted_by_key




def stations_level_over_threshold(stations,tol):
    list_of_tup = []
    for station in stations:
        if station.typical_range_consistent() == True:
            if station.latest_level != None and station.relative_water_level() > tol:
                tup = (station,station.relative_water_level())
                list_of_tup.append(tup)
    list_of_tup_sorted = sorted_by_key(list_of_tup,1,True)
    return list_of_tup_sorted

def stations_highest_rel_level(stations, N):
    list_of_tup = []
    for station in stations:
        if station.typical_range_consistent() == True and station.relative_water_level() != None:
            tup = (station,station.relative_water_level())
            list_of_tup.append(tup)
    list_of_tup_sorted = sorted_by_key(list_of_tup,1,True)[:N]
    risk_stations = []
    for tup in list_of_tup_sorted:
        risk_stations.append(tup[0])
    return risk_stations
