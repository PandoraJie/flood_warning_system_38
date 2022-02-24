#plots the water levels over the past 10 days for the 5 stations
#at which the current relative water level is greatest

import matplotlib.pyplot as plt
from stationdata import build_station_list, update_water_levels
from flood import stations_highest_rel_level
from plot import plot_water_levels
from datafetcher import fetch_measure_levels
import datetime

stations = build_station_list()
update_water_levels(stations)
risk_stations = stations_highest_rel_level(stations,5)
dt = 10
dates = []
levels = []
for station in risk_stations:
    date, level = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
    dates.append(date)
    levels.append(level)

plot_water_levels(risk_stations,dates,levels)