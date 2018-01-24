"""
Gera uma lista de pontos 2D

Modo de uso:

digite no terminal "python3 genpoints.py <n> <l> <r>"
onde:
    n é o número de pontos
    l é o menor valor para as coordenada x, y
    r é o maior valor para a coordenada x, y

para salvar a saída em um arquivo digite no terminal:
    "python3 genpoints.py <n> <l> <r> > <arquivo.txt>"
"""


import sys
from random import uniform


def genpoints (n, r):
    """
    Gera uma lista de pontos 2D com n pontos
    :param n: O número de pontos a serem gerados
        :type n: int
    :param r: Uma tupla com o limite inferior e superior para as coordenadas X e Y.
        :type r: (float, float)
    :return: Uma lista de pontos
        :rtype: [(float, float)]
    """
    points = [(uniform(r[0], r[1]), uniform(r[0], r[1])) for _ in range(n)]
    for a, b in points:
        print(a, b)


if __name__ == '__main__':
    genpoints(int(sys.argv[1]), (float(sys.argv[2]), float(sys.argv[3])))
