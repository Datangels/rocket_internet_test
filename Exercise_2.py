# -*- coding: utf-8 -*-
import unittest


class Test(unittest.TestCase):
    def __init__(self):
        self.assertEqual(have_overlap([(0, 0), (24, 0)], [(0, 0), (12, 0)]), True)  # Exercise example
        self.assertEqual(have_overlap([(0, 0), (12, 0)], [(0, 0), (24, 0)]), True)  # Exercise example reverse
        self.assertEqual(have_overlap([(11, 0), (24, 0)], [(0, 0), (10, 0)]), False)  # Exercise example
        self.assertEqual(have_overlap([(0, 0), (10, 0)], [(11, 0), (24, 0)]), False)  # Exercise example reverse
        self.assertEqual(have_overlap([(1, 0), (1, 10)], [(1, 9), (24, 0)]), True)  # One minute overlap
        self.assertEqual(have_overlap([(1, 9), (24, 0)], [(1, 0), (1, 10)]), True)  # One minute overlap reverse
        self.assertEqual(have_overlap([(11, 10), (11, 58)], [(11, 59), (12, 10)]), False)  # One minute difference
        self.assertEqual(have_overlap([(11, 59), (12, 10)], [(11, 10), (11, 58)]), False)  # One minute difference reverse
        self.assertEqual(have_overlap([(0, 0), (12, 28)], [(12, 28), (14, 00)]), True)  # Same minute start end
        self.assertEqual(have_overlap([(12, 28), (14, 00)], [(0, 0), (12, 28)]), True)  # Same minute start end reverse

        self.assertEqual(have_overlap([(0, 0), (23, 59)], [(0, 0), (23, 59)]), True)  # All day


def convert_range(t_interval):
    """
    A day contains 1440 minutes.
    This function converts the range (hour, minute) to its corresponding quantity of minutes.
    The number of hours are multiply for 60, this means the conversion from hours to minutes.
    After that the quantity of minute is add in order to obtain the total amount of minutes.
    Example: [(11, 0), (24, 0)] --> [660, 1440]
    :param t_interval: list of set
    :return: list of int
    """
    return [60 * time[0] + time[1] for time in t_interval]


def sort_ranges(time_range_1, time_range_2):
    """
    Given two times ranges, return first the earlier and then the latest.
    :param time_range_1: list of int
    :param time_range_2: list of int
    :return: list of int, list of int
    """
    if time_range_1[0] <= time_range_2[0]:
        return time_range_1, time_range_2
    else:
        return time_range_2, time_range_1


def compare_ranges(time_range_1, time_range_2):
    """
    This logic assumes that the lowest time range can be both on first or second position.
    Example:
    time_range_1 = [660, 1440] --> it starts from the minute 660 until the minute 1440.
    time_range_2 = [0, 600] --> it starts from the minute 0 until the minute 600.
    Is 660 equal or lower than 600? False
    Is 1440 equal or lower than 0? False
    The time ranges do not overlap.
    :param time_range_1: list of int
    :param time_range_2: list of int 
    :return: boolean
    """
    if time_range_1[1] >= time_range_2[0]:
        return True
    else:
        return False


def have_overlap(t_interval_1, t_interval_2):
    """
    Given​ ​two​ ​time​ ​intervals​ ​returns​ ​whether​ ​they​ ​overlap.​
    :param t_interval_1: list of set
    :param t_interval_2: list of set 
    :return: boolean
    """
    # Convert time range in a more manageable way
    time_range_1 = convert_range(t_interval_1)
    time_range_2 = convert_range(t_interval_2)

    # Sort the time ranges from the earliest to the latest
    time_range_1, time_range_2 = sort_ranges(time_range_1, time_range_2)

    # Apply comparison logic
    return compare_ranges(time_range_1, time_range_2)


if __name__ == '__main__':
    unittest.main()
