import matplotlib.pyplot as plt
from datapoint import DataPoint


class Map:
    def __init__(self, timestamp, size: tuple, datapoints: list[DataPoint]):
        self.timestamp = timestamp
        self.size = size
        self.datapoints = datapoints

    def plot(self):
        plt.xlim(0, map.size[0])
        plt.ylim(0, map.size[1])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('')

