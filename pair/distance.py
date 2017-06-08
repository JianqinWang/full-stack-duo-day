#!/usr/bin/python3

def MinDistance2D(coords=[]):
    i = len(coords)
    tempmin = -1

    for first in range(i):
        for second in range(first + 1, i):
            temp = (coords[first][0] - coords[second][0])**2 + (coords[first][1] - coords[second][1])**2
            if (tempmin < 0 or tempmin > temp):
                tempmin = temp
                coord1 = coords[first]
                coord2 = coords[second]
    print("Closest pair is {} and {}".format(coord1, coord2))
    return (coord1, coord2)

MinDistance2D([(0, 0), (1, 5), (3, 2), (5, 6)])

def MinDistance3D(coords=[]):
    i = len(coords)
    tempmin = -1

    for first in range(i):
        for second in range(first + 1, i):
            temp = (coords[first][0] - coords[second][0])**2 + (coords[first][1] - coords[second][1])**2 + (coords[first][2] - coords[second][2])**2
            if (tempmin < 0 or tempmin > temp):
                tempmin = temp;
                coord1 = coords[first]
                coord2 = coords[second]
    print("Closest pair is {} and {}".format(coord1, coord2))
    return (coord1, coord2)

MinDistance3D([(0, 0, 0), (1, 1, 1), (1 ,2 ,1), (2, 1, 3)])
