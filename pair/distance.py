#!/usr/bin/python3
"""
Python functions for finding minimum distanec between two coordinates
"""


def MinDistance2D(coords=[]):
    """
    find minimum distance within 2d array
    """
    i = len(coords)
    tempmin = -1

    if (i <= 1):
        print("Please input at least a pair of coordinates")
        return
    if (type(coords[0]) is not list and type(coords[0]) is not tuple):
        print("Please give a list of lists (x, y coords) or list of tuples")
        return
    for first in range(i):
        for second in range(first + 1, i):
            if (len(coords[first]) != 2 or len(coords[second]) != 2):
                print("Please make sure your input is correct for coordinates")
                return
            temp = (abs(coords[first][0] - coords[second][0]) +
                    abs(coords[first][1] - coords[second][1]))
            if (tempmin < 0 or tempmin > temp):
                tempmin = temp
                coord1 = coords[first]
                coord2 = coords[second]
    print("Closest pair is {} and {}".format(coord1, coord2))
    return (coord1, coord2)

MinDistance2D([(0, 0), (1, 5), (3, 2), (5, 6)])
MinDistance2D("TEST")
MinDistance2D([(0, 0)])
MinDistance2D(["one", "two", "three"])

def MinDistance3D(coords=[]):
    """
    find minimum distance within 3d array
    """
    i = len(coords)
    tempmin = -1

    if (i <= 1):
        print("Please input at least a pair of coordinates")
        return
    if (type(coords[0]) is not list and type(coords[0]) is not tuple):
        print("Please give a list of lists (x, y, z coords) or list of tuples")
        return
    for first in range(i):
        for second in range(first + 1, i):
            if (len(coords[first]) != 3 or len(coords[second]) != 3):
                print("Please make sure your input is correct for coordinates")
                return
            temp = (abs(coords[first][0] - coords[second][0]) +
                    abs(coords[first][1] - coords[second][1]) +
                    abs(coords[first][2] - coords[second][2]))
            if (tempmin < 0 or tempmin > temp):
                tempmin = temp
                coord1 = coords[first]
                coord2 = coords[second]
    print("Closest pair is {} and {}".format(coord1, coord2))
    return (coord1, coord2)

MinDistance3D([(0, 0, 0), (1, 1, 1), (1, 2, 1), (2, 1, 3)])
MinDistance2D("Test")
MinDistance2D([(9, 9, 9)])
MinDistance2D(["one", "two", "three"])
