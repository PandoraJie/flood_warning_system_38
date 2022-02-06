from pickle import NONE
from floodsystem.stationdata import build_station_list

def typical_range_consistent(self):
    r1 = self(1)
    r0 = self(0)

    if self == None:
        return False
    elif r1 >= r0:
        return True
    else:
        return False

def inconsistent_typical_range_stations(stations):
    incon_stations = []
    for station in stations:
        if typical_range_consistent(station.typical_range) == False:
            incon_stations.append(station.name)
    return incon_stations