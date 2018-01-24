import sys
from utils import *


def distances(points: [(float, float)]) -> [((float, float), (float, float), float)]:
    """
    Calcula a distância entre todas as combinações de pontos possíveis, i.e. usando força bruta
    :param points: Uma lista de tuplas, onde cada tupla é um ponto com coordenadas X e Y.
    :return: Retorna uma lista ordenada pelas distâncias com seus respectivos pontos
    """
    n = len(points)
    d = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            a, b = points[i], points[j]
            d.append((a, b, euclideandst(a, b)))
    # Ordena a lista pelas distâncias
    return sorted(d, key=lambda x: x[2])


def distancesDC(points: [(float, float)]) -> ((float, float), (float, float), float):
    """
    Calcula a distância entre todas as combinações de pontos possíveis utilizando divisão e conquista
    :param points: Uma lista de tuplas, onde cada tupla é um ponto com coordenadas X e Y.
    :return: Retorna os dois pontos tais que a distância entre eles é a menor possível
    """

    n = len(points)
    if n <= 3:
        return distances(points)[0]

    # Ordena os pontos pela coordenada x
    sorted_points = sorted(points, key=lambda x: x[0])
    midpoint = sorted_points[n//2]

    left = sorted_points[:5//2]
    right = sorted_points[5//2:]

    d = min(
        distancesDC(left),
        distancesDC(right),
        key=lambda x: x[2])

    strip = []

    for p in sorted_points:
        if abs(p[0] - midpoint[0]) < d[2]:
            strip.append(p)

    return min(
        d,
        stripclosest(strip, d[2]),
        key=lambda x: x[2]
    )


if __name__ == '__main__':
    points = []
    for line in sys.stdin:
        a, b = [t(s) for t, s in zip((float, float), line.split())]
        points.append((a, b))

    p1 = p2 = dist = None

    if int(sys.argv[1]) == 0:
        p1, p2, dist = distances(points)[0]
    elif int(sys.argv[1]) == 1:
        p1, p2, dist = distancesDC(points)

    print(p1, p2, dist, sep='\n')
    print('A = ({0:s}, {1:s})'.format(str(p1[0]), str(p1[1])))
    print('B = ({0:s}, {1:s})'.format(str(p2[0]), str(p2[1])))
    print('Distance: {0:s} u.m'.format(str(dist)))
