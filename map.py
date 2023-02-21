import matplotlib.pyplot as plt
from datapoint import DataPoint


class Map:
    def __init__(self, timestamp, upper_left: tuple, size: tuple, datapoints: list[DataPoint]):
        self.timestamp = timestamp
        self.upper_left = upper_left
        self.size = size
        self.bottom_right = ([sum(x) for x in zip(self.upper_left, self.size)])
        self.datapoints = datapoints

    def plot(self):
        plt.xlim(self.upper_left[0], self.bottom_right[0])
        plt.ylim(self.upper_left[1], self.bottom_right[1])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'map at time stamp {self.timestamp}')
        plt.scatter(
            [datapoint.position[0] for datapoint in self.datapoints],
            [datapoint.position[1] for datapoint in self.datapoints]
        )
        plt.show()


