import datetime
import matplotlib.dates


from datafetcher import fetch_measure_levels
from plot import plot_water_level_with_fit
from stationdata import build_station_list, update_water_levels
from flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)
risk_stations = stations_highest_rel_level(stations,5)

dt = 2

for station in risk_stations:
    dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
    for i in range(len(levels)):
        if levels[i] == None:
            levels[i] = 0
    try:
        plot_water_level_with_fit(station, dates, levels, 4)
    except:
        print("Error:{}".format(station.name))