# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import numpy as np
from station import MonitoringStation
from haversine import haversine
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

#hl600
#def rivers_by_station_number(stations, N):
#    river_station_number = []
#    for station in stations:
#            if station.river not in river_station_number:
#                name_of_river = station.river
#                number = 0
#            for station in stations:
#                if station.river == name_of_river:
#                    number += 1
#          river_station_number.append((name_of_river, number))
#    river_station_number = sorted_by_key(river_station_number, 1, reverse = True)
#    append_list = river_station_number[:N]
#    return append_list

#Revised
def rivers_by_station_number(stations, N):
    station_number_tup =  []
    dic = stations_by_river(stations)
    for river in dic.keys():
        tup = (river,len(dic[river]))
        station_number_tup.append(tup)
    station_number_tup_sorted = sorted_by_key(station_number_tup,1,True)
    while station_number_tup_sorted[N-1][1] == station_number_tup_sorted[N][1]:
        N += 1
    return station_number_tup_sorted[:N]

#Task 1F

#hl600
#def inconsistent_typical_range_stations(stations):
#    incon_stations = []
#    for station in stations:
#        if station.typical_range_consistent() == False:
#            incon_stations.append(station.name)
#    return incon_stations

#Revised
def inconsistent_typical_range_stations(stations):
    inconsistent_list = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent_list.append(station)
    return inconsistent_list