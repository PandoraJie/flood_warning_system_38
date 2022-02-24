import matplotlib.pyplot as plt
from datetime import datetime, timedelta
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