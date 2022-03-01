from analysis import polyfit
from stationdata import build_station_list, update_water_levels
import datetime
import random




def test_polyfit():
    t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]
    levels = [random.randint(0, 9) for p in range(7)]
    tup = polyfit(dates, levels, 4)
    poly,d0 = tup
    assert tup
    assert type(tup) == tuple
    assert poly
    assert d0
    assert type(d0) == float