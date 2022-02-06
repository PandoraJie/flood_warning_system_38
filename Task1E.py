from sqlalchemy import false, true
from floodsystem.stationdata import build_station_list

def rivers_by_station_number(stations, N):
    river_station_number = []
    for station in stations:
        if station.river not in river_station_number:
          name_of_river = stations.river
          number = 0
          for station in stations:
              if stations.river == name_of_river:
                  number += 1
          river_station_number.append((number,name_of_river))
    river_station_number = river_station_number.sorted()
    river_station_number = river_station_number.reverse()
    append_list = []
    for sorted_stations in river_station_number:
      if sorted_stations(0) >= river_station_number[N](0):
          append_list.append((sorted_stations(1),sorted_stations(0)))
    return append_list
