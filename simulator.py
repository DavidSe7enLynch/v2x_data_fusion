from typing import List, Tuple


def data_fusion(maps: List[Tuple[int, List[Tuple[float, float, float, float]]]]) -> List[
    List[Tuple[int, Tuple[float, float, float, float]]]]:
    """
    Performs data fusion for maps received from multiple cars in a V2X scenario.
    :param maps: A list of tuples containing the time stamp and a list of data points for each map received.
    :return: A list of lists, where each inner list contains tuples representing data points that belong to the same car.
    """
    # Combine all data points from all maps into a single list
    all_data_points = []
    for map in maps:
        time_stamp, data_points = map
        all_data_points += [(time_stamp, i, dp) for i, dp in enumerate(data_points)]

    # Sort the combined list of data points by their GPS location
    all_data_points.sort(key=lambda x: x[2][:2])

    # Group together data points that are close to each other in space and time
    grouped_data_points = []
    last_group = []
    last_point = None
    for time_stamp, index, point in all_data_points:
        if last_point is not None and (time_stamp - last_point[0] <= 1) and (point[0] - last_point[2][0] <= 10) and (
                point[1] - last_point[2][1] <= 10):
            last_group.append((index, point))
        else:
            if last_group:
                grouped_data_points.append(last_group)
            last_group = [(index, point)]
        last_point = (time_stamp, index, point)
    if last_group:
        grouped_data_points.append(last_group)

    # Return the grouped data points
    return grouped_data_points
