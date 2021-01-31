#!/usr/bin/python3.8
import sys


def gray_code(n):
    if n <= 0:
        return []
    if n == 1:
        return ['0', '1']
    res = gray_code(n - 1)
    print(n, res, res[::-1])
    return ['0' + s for s in res] + ['1' + s for s in res[::-1]]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        gray_code(int(sys.argv[1]))