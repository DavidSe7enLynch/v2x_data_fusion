import simulator

from datapoint import DataPoint
from map import Map


def test_simulator():
    map1 = (1, [(1.0, 2.0, 3.0, 4.0), (3.0, 4.0, 5.0, 6.0)])
    map2 = (2, [(5.0, 6.0, 7.0, 8.0), (7.0, 8.0, 9.0, 10.0)])
    map3 = (3, [(2.0, 3.0, 4.0, 5.0), (6.0, 7.0, 8.0, 9.0)])
    maps = [map1, map2, map3]

    grouped_data_points = simulator.data_fusion(maps)
    print(grouped_data_points)


def test_map():
    datapoint1 = DataPoint()
    map1 = Map(
        timestamp=10,
        upper_left=(0, 0),
        size=(100, 100),
        datapoints=[])
