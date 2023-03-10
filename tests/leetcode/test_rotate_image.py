from leetcode.lc_048_rotate_image import Solution


def _check(m, expected):
    ret = Solution().rotate(m)
    for l1, l2 in zip(m, expected):
        for a, b in zip(l1, l2):
            assert (
                a == b
            ), f"Wrong answer for input {repr(m)}. Expected: {expected}. Returned: {ret}"


def test_1():
    m = []
    e = []
    _check(m, e)


def test_2():
    m = [[1]]
    e = [[1]]
    _check(m, e)


def test_3():
    m = [
        [1, 2],
        [3, 4],
    ]
    e = [
        [3, 1],
        [4, 2],
    ]
    _check(m, e)


def test_4():
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    e = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    _check(m, e)


def test_5():
    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    e = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]
    _check(m, e)


def test_6():
    m = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    e = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]
    _check(m, e)


def test_7():
    m = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36],
    ]
    e = [
        [31, 25, 19, 13, 7, 1],
        [32, 26, 20, 14, 8, 2],
        [33, 27, 21, 15, 9, 3],
        [34, 28, 22, 16, 10, 4],
        [35, 29, 23, 17, 11, 5],
        [36, 30, 24, 18, 12, 6],
    ]
    _check(m, e)


def test_8():
    m = [
        [1, 2, 3, 4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20, 21],
        [22, 23, 24, 25, 26, 27, 28],
        [29, 30, 31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40, 41, 42],
        [43, 44, 45, 46, 47, 48, 49],
    ]
    e = [
        [43, 36, 29, 22, 15, 8, 1],
        [44, 37, 30, 23, 16, 9, 2],
        [45, 38, 31, 24, 17, 10, 3],
        [46, 39, 32, 25, 18, 11, 4],
        [47, 40, 33, 26, 19, 12, 5],
        [48, 41, 34, 27, 20, 13, 6],
        [49, 42, 35, 28, 21, 14, 7],
    ]
    _check(m, e)


def test_9():
    m = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, 29, 30, 31, 32],
        [33, 34, 35, 36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45, 46, 47, 48],
        [49, 50, 51, 52, 53, 54, 55, 56],
        [57, 58, 59, 60, 61, 62, 63, 64],
    ]
    e = [
        [57, 49, 41, 33, 25, 17, 9, 1],
        [58, 50, 42, 34, 26, 18, 10, 2],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [63, 55, 47, 39, 31, 23, 15, 7],
        [64, 56, 48, 40, 32, 24, 16, 8],
    ]
    _check(m, e)


def test_10():
    m = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14, 15, 16, 17, 18],
        [19, 20, 21, 22, 23, 24, 25, 26, 27],
        [28, 29, 30, 31, 32, 33, 34, 35, 36],
        [37, 38, 39, 40, 41, 42, 43, 44, 45],
        [46, 47, 48, 49, 50, 51, 52, 53, 54],
        [55, 56, 57, 58, 59, 60, 61, 62, 63],
        [64, 65, 66, 67, 68, 69, 70, 71, 72],
        [73, 74, 75, 76, 77, 78, 79, 80, 81],
    ]
    e = [
        [73, 64, 55, 46, 37, 28, 19, 10, 1],
        [74, 65, 56, 47, 38, 29, 20, 11, 2],
        [75, 66, 57, 48, 39, 30, 21, 12, 3],
        [76, 67, 58, 49, 40, 31, 22, 13, 4],
        [77, 68, 59, 50, 41, 32, 23, 14, 5],
        [78, 69, 60, 51, 42, 33, 24, 15, 6],
        [79, 70, 61, 52, 43, 34, 25, 16, 7],
        [80, 71, 62, 53, 44, 35, 26, 17, 8],
        [81, 72, 63, 54, 45, 36, 27, 18, 9],
    ]
    _check(m, e)
