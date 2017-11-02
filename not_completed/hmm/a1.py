import math


def closestLocations(totalCrates, allLocations, truckCapacity):
    distance_map = [0] * totalCrates

    for i in range(0, totalCrates):
        distance_map[i] = getDistance(allLocations[i]), allLocations[i]

    distance_map = sorted(distance_map, key=lambda x: x[0])

    print([l[1] for l in distance_map[:truckCapacity]])


def getDistance(location):
    return math.sqrt(location[0] * location[0] + location[1] * location[1])


closestLocations(3, [[1, 2], [3, 4], [1, -1]], 2)
