import datetime


from datafetcher import fetch_measure_levels
from plot import plot_water_level_with_fit
from stationdata import build_station_list, update_water_levels
from flood import stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)
risk_stations = stations_highest_rel_level(stations,5)

dates = []
levels = []

for station in risk_stations:
    date, level = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=2))
    dates.append(date)
    levels.append(level)
    plot_water_level_with_fit(station, dates, levels, 4)