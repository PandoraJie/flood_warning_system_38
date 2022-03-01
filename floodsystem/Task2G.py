
from datafetcher import fetch_measure_levels
from plot import plot_water_level_with_fit
from stationdata import build_station_list, update_water_levels
from flood import stations_highest_rel_level
from analysis import polyfit
from flood import stations_level_over_threshold, stations_highest_rel_level
import datetime
import matplotlib.dates
from utils import sorted_by_key
import numpy as np

stations = build_station_list()
update_water_levels(stations)

#If the water level is increasing in the past 2 days
def forecast_increase(station):
    dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=2))
    x0 = matplotlib.dates.date2num(dates)
    x1 = np.linspace(x0[0],x0[-1],len(x0))
    #calculate best-fit line and check gradient at the last day
    slope = np.poly1d(np.polyfit(x1 - x0[0], levels, 4))
    #if gradient is positive, water level is increasing
    if slope(x1[-1]) > 0:
        return True
    #if gradient is negative, water level is not increasing
    else:
        return False

#risks: list of tuples (station.name,risk_level)
risks = []
#rel_levels: list of tuples (station, relative_water_level)
rel_levels = []
#sort stations according to relative water level
for station in stations:
    if station.relative_water_level() != None:
        rel_levels.append((station,station.relative_water_level()))
        rel_levels_sorted = sorted_by_key(rel_levels,1,True)

#check relative water level of every station and assess risk level
for data in rel_levels_sorted:
    station = data[0]
    try:
        if data[1] >= 0.7:
            if forecast_increase(station):
                #if relative water level is bigger than 0.7 and water level is increasing, Severe
                risks.append((station.name,"Severe"))
            else:
                #if relative water level is bigger than 0.7 but water level is not increasing, High
                risks.append((station.name,"High"))
        elif 0.5 <= data[1] < 0.7:
            #if relative water level is between 0.5 and 0.7, Moderate
            risks.append((station.name,"Moderate"))
        else:
            #if relative water level is lower than 0.5, Low
            risks.append((station.name,"Low"))
    except:
        #if data are not complete, report error
        print("Error:{}".format(station.name))

#severe: list of towns with risk "Severe"
severe = []
for risk in risks:
    if risk[1] == "Severe":
        severe.append(risk)
print(severe)