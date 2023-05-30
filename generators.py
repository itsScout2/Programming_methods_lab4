from random import randint
import time

def standart_random(size: int) -> list:

    """
    Встроенный генератор псевдослучайных последовательностей [0, 16383]

    :param size: количество генерируемых чисел
    :type size: int
    :return: список псевдослучайных чисел
    :rtype: list
    """

    result = []
    for i in range(size):
        result.append(randint(0, 16384))
    return result

def LCG(size: int) -> list:

    """
    Линейный конгруэнтный метод [0, 16383]

    :param size: количество генерируемых чисел
    :type size: int
    :return: список псевдослучайных чисел
    :rtype: list
    """

    result = []

    m = (1 << 63) - 1
    k = 1 << 63
    b = int(time.perf_counter_ns() // 100)
    if b == m:
        b -= 1
    r0 = 13

    for i in range(size):
        r0 = (k * r0 + b) % m
        result.append(r0 % 16384)

    return result

def mid_compositions(size: int) -> list:

    """
    Метод серединных произведений [0, 16383]

    :param size: количество генерируемых чисел
    :type size: int
    :return: список псевдослучайных чисел
    :rtype: list
    """

    result = []
    r0 = int(time.time()) % 128 + 1
    r1 = int(time.time()) % 128 + 1
    b = 11

    for i in range(size):
        r = (r0 * r1 * b) & 16383
        result.append(r)
        r0 = r1
        r1 = r
        r0 += 13
        r1 += 17
        b += 2
    return result

