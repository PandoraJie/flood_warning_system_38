stations = build_station_list()
update_water_levels(stations)


dates = []
levels = []
threshold = 

for station in stations:
    date, level = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=2))
    dates.append(date)
    levels.append(level)
    forecast_function = polyfit(dates, levels, p)[0]
    x0 = matplotlib.dates.date2num(dates)
    date_today = matplotlib.dates.date2num()


    if forecast_function(date_today + 1 - x0[0]) > threshold:
        risk = "severe"
    elif forecast_function(date_today + 3 - x0[0]) > threshold:
        risk = "high"
    elif forecast_function(date_today + 7 - x0[0]) > threshold:
        risk = "moderate"
    else:
        risk = "low"

    