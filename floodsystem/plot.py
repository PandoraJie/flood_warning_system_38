import matplotlib.dates
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

import numpy as np
from analysis import polyfit
from stationdata import build_station_list, update_water_levels
from flood import stations_level_over_threshold


def plot_water_levels(station, dates, levels):
    plt.plot(dates,levels)
    plt.xlabel('Date')
    plt.ylabel('Water level / m')
    plt.xticks(rotation=45);
    plt.title(station.name)
    min = []
    max = []
    for i in range(len(dates)):
        min.append(station.typical_range[0])
        max.append(station.typical_range[1])
    plt.plot(dates, min, label='Min')
    plt.plot(dates, max, label='Max')
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x0 = matplotlib.dates.date2num(dates)
    plt.plot(x0,levels,label='Data')
    plt.xlabel('Date')
    plt.ylabel('Water level / m')
    min = []
    max = []
    for i in range(len(dates)):
        min.append(station.typical_range[0])
        max.append(station.typical_range[1])
    plt.plot(dates, min, label='Min')
    plt.plot(dates, max, label='Max')
    x1 = np.linspace(x0[0],x0[-1],len(x0))
    poly = np.poly1d(np.polyfit(x1 - x0[0], levels, p))
    plt.plot(x1, poly(x1 - x0[0]),label='Best-Fit')
    plt.title(station.name)
    plt.tight_layout()
    plt.show()