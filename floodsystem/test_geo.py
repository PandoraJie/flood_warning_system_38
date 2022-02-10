
from stationdata import build_station_list
from geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number, inconsistent_typical_range_stations

def test_stations_by_distance():
    #testcall
    #sorted_list = stations_by_distance(stations,cam)
    stations = build_station_list()
    cam = (52.2053, 0.1218)
    closest_10 = stations_by_distance(stations,cam)[:10]
    result = [('Cambridge Jesus Lock', 0.840237595667494), ('Bin Brook', 2.502277543239629), ("Cambridge Byron's Pool", 4.07204948005424), ('Cambridge Baits Bite', 5.115596582531859), ('Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 7.0443978959918025), ('Oakington', 7.12825901765745), ('Stapleford', 7.265704342799649), ('Comberton', 7.735085060177142), ('Dernford', 7.993872393303291)]
    assert closest_10 == result



def test_stations_within_radius():
    #testcall
    #list_of_stations_within = stations_within_radius(stations,cam,10)
    stations = build_station_list()
    cam = (52.2053, 0.1218)
    list_of_stations_within = stations_within_radius(stations,cam,10)
    result = ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
    assert list_of_stations_within == result