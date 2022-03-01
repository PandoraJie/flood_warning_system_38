from flood import stations_level_over_threshold,stations_highest_rel_level
from stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold():
    stations = build_station_list()[:10]
    update_water_levels(stations)
    list_of_tup = stations_level_over_threshold(stations,-1)
    assert list_of_tup
    assert type(list_of_tup) == list
    assert len(list_of_tup) == 10
    for i in range(9):
        assert list_of_tup[i][1] >= list_of_tup[i+1][1]

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    list_of_tup = stations_highest_rel_level(stations,10)
    assert list_of_tup
    assert type(list_of_tup) == list
    assert len(list_of_tup) == 10
    for i in range(9):
        assert list_of_tup[i][1] >= list_of_tup[i+1][1]