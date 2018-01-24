"""
Arquivo para criar as baterias de testes
"""

import sys
from os import system


def main():
    points_per_set = 10
    npoints = [5, 10, 20, 50, 100, 200, 500, 1000, 5000, 10000]

    system("rm -rf tests/")
    system("mkdir tests/")

    for n in npoints:
        system("mkdir tests/{0}".format(n))
        for i in range(points_per_set):
            system("python3 genpoints.py {0} -1000 1000 > tests/{1}/{2}.txt".format(n, n, i+1))


if __name__ == '__main__':
    main()
    sys.exit(0)
