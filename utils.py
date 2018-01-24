import math


def stripclosest(points, d):
    sorted_points = sorted(points, key=lambda x: x[1])
    n = len(sorted_points)
    _min = d

    p1 = p2 = None

    for i in range(n):
        for j in range(i + 1, n):
            if (sorted_points[j][1] - sorted_points[i][1]) >= _min:
                break

            dist = euclideandst(sorted_points[i], sorted_points[j])
            if dist < _min and dist != 0:
                _min = dist
                p1 = sorted_points[i]
                p2 = sorted_points[j]

    return p1, p2, _min


def euclideandst(a, b):
    xa, ya = a
    xb, yb = b
    return math.sqrt((xb - xa)**2 + (yb - ya)**2)
