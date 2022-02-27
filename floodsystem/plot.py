import matplotlib
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
    plt.tight_layout()
    plt.show()
#typical highs&lows still not included

def plot_water_level_with_fit(station, dates, levels, p):
    x0 = matplotlib.dates.date2num(dates)
    plt.plot(x0,levels)
    plt.xlabel('Date')
    plt.ylabel('Water level / m')
    x1 = np.linspace(x0[0], x0[-1], 30)
    poly = polyfit(dates, levels, p)[0]
    plt.plot(x1, poly(x1 - x0[0]))
    plt.title(station.name)
    plt.tight_layout()
    plt.show()