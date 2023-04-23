from mandatory_assigments.course_schedule_III import Solution


def test_1():
    assert Solution().findOrder(2, [[1, 0]]) == [0, 1]


def test_2():
    assert Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]


def test_3():
    assert Solution().findOrder(1, []) == [0]


def test_4():
    assert Solution().findOrder(2, [[1, 0], [0, 1]]) == []


def test_5():
    assert Solution().findOrder(3, [[1, 0], [1, 2], [0, 1]]) == []
