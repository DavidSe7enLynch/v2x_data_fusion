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
    datapoint1 = DataPoint(position=(10, 40), velocity=(2, -1), size=(3, 5))
    datapoint2 = DataPoint(position=(5, 80), velocity=(-3, -4), size=(6, 3))
    map1 = Map(
        timestamp=10,
        upper_left=(0, 0),
        size=(100, 100),
        datapoints=[datapoint1, datapoint2]
    )
    map2 = Map(
        timestamp=20,
        upper_left=(5, 5),
        size=(100, 100),
        datapoints=[datapoint2, datapoint1]
    )
    map1.plot()
    map2.plot()


if __name__ == '__main__':
    test_map()
    print("finished")

