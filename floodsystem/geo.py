# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import numpy as np
from haversine import haversine, Unit
from utils import sorted_by_key  # noqa


#Task 1B
def stations_by_distance(stations, p):
    list_of_tuples=[]
    for station in stations:
        element = (station.name,haversine(station.coord,p))
        list_of_tuples.append(element)
    sorted_list = sorted_by_key(list_of_tuples,1)
    return sorted_list

#Task 1C
def stations_within_radius(stations, centre, r):
    list_of_stations_within = []
    for station in stations:
        if haversine(station.coord,centre) <= r:
            list_of_stations_within.append(station)
    return list_of_stations_within

#Task 1D
def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    dic = {}
    for station in stations:
        if station.river in dic.keys():
            dic[station.river].append(station.name)
        else:
            dic.setdefault(station.river,[]).append(station.name) 
    return dic

#Task 1E
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

#Task 1F
def inconsistent_typical_range_stations(stations):
    incon_stations = []
    for station in stations:
        if typical_range_consistent(station.typical_range) == False:
            incon_stations.append(station.name)
    return incon_stations