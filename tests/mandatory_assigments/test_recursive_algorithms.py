from functools import wraps
import random
from itertools import combinations
import pytest

import mandatory_assigments.recursive_algorithms as recursive_algorithms


# SETUP

# Decorate functions


def count_calls(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        decorator.calls += 1
        return func(*args, **kwargs)

    decorator.calls = 0

    return decorator


for (
    func_name
) in "list_sum, digit_sum, tree_sum, tree_max, k_combinations, all_strictly_increasing_sequences, create_pattern, find_middle_rec".split(
    ","
):
    func_name = func_name.strip()
    setattr(
        recursive_algorithms,
        func_name,
        count_calls(getattr(recursive_algorithms, func_name)),
    )

# TEST TOOLS


def randlist(size, minval=-100, maxval=100):
    return [random.randint(minval, maxval) for _ in range(size)]


# TESTS


@pytest.mark.parametrize("numbers", [randlist(list_len) for list_len in range(10)])
def test_list_sum_for(numbers):
    recursive_algorithms.list_sum.calls = 0

    expected = sum(numbers)
    returned = recursive_algorithms.list_sum(numbers)

    assert (
        expected == returned
    ), f"Wrong answer for list {numbers}. Expected: {expected}. Returned: {returned}."
    assert recursive_algorithms.list_sum.calls >= len(
        numbers
    ), "Function list_sum is not recursive"


@pytest.mark.parametrize(
    "n",
    [
        123,
        9876543210,
        101010,
        0,
        4,
        142353,
        9999999999,
        234968,
        29876452938745,
        91919191919,
    ],
)
def test_digit_sum_for(n):
    recursive_algorithms.digit_sum.calls = 0

    expected = sum(int(d) for d in str(n))
    returned = recursive_algorithms.digit_sum(n)

    assert (
        expected == returned
    ), f"Wrong answer for {n}. Expected: {expected}. Returned: {returned}."
    assert recursive_algorithms.digit_sum.calls >= len(
        str(n)
    ), "Function digit_sum is not recursive"


@pytest.mark.parametrize(
    "elements",
    [randlist(list_len, -9, 9) for list_len in list(range(5)) + list(range(5, 20, 3))],
)
def test_tree_sum_for(elements):
    recursive_algorithms.tree_sum.calls = 0

    tree = recursive_algorithms.Tree(elements)

    expected = sum(elements)
    returned = recursive_algorithms.tree_sum(tree.root)

    assert (
        expected == returned
    ), f"Wrong answer for tree with elements {elements}. Expected: {expected}. Returned: {returned}."
    assert recursive_algorithms.tree_sum.calls >= len(
        elements
    ), "Function tree_sum is not recursive"


@pytest.mark.parametrize(
    "elements",
    [randlist(list_len, -9, 9) for list_len in list(range(5)) + list(range(5, 20, 3))],
)
def test_tree_max_for(elements):
    recursive_algorithms.tree_max.calls = 0

    tree = recursive_algorithms.Tree(elements)

    expected = max(elements) if elements else -float("inf")
    returned = recursive_algorithms.tree_max(tree.root)

    assert (
        expected == returned
    ), f"Wrong answer for tree with elements {elements}. Expected: {expected}. Returned: {returned}."
    assert recursive_algorithms.tree_max.calls >= len(
        elements
    ), "Function tree_max is not recursive"


@pytest.mark.parametrize(
    "list_len, k",
    [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (5, 2), (5, 3), (9, 2), (9, 4)],
)
def test_k_combinations_for(list_len, k):
    recursive_algorithms.k_combinations.calls = 0

    l = randlist(list_len)

    expected = list(combinations(l, k))
    returned = recursive_algorithms.k_combinations(l, k)

    assert len(expected) == len(
        returned
    ), f"Wrong answer for list={l} and k={k}. Expected: {expected}. Returned: {returned}."

    expected = sorted([tuple(sorted(e)) for e in expected])
    returned = sorted([tuple(sorted(r)) for r in returned])

    assert (
        returned == expected
    ), f"Wrong answer for list={l} and k={k}. Expected: {expected}. Returned: {returned}."
    assert recursive_algorithms.k_combinations.calls >= min(
        list_len, k
    ), "Function k_combinations is not recursive"


@pytest.mark.parametrize(
    "k, n, expected",
    [
        (2, 3, [[1, 2], [1, 3], [2, 3]]),
        (1, 1, [[1]]),
        (10, 3, []),
        (4, 4, [[1, 2, 3, 4]]),
        (
            3,
            7,
            [
                [1, 2, 3],
                [1, 2, 4],
                [1, 2, 5],
                [1, 2, 6],
                [1, 2, 7],
                [1, 3, 4],
                [1, 3, 5],
                [1, 3, 6],
                [1, 3, 7],
                [1, 4, 5],
                [1, 4, 6],
                [1, 4, 7],
                [1, 5, 6],
                [1, 5, 7],
                [1, 6, 7],
                [2, 3, 4],
                [2, 3, 5],
                [2, 3, 6],
                [2, 3, 7],
                [2, 4, 5],
                [2, 4, 6],
                [2, 4, 7],
                [2, 5, 6],
                [2, 5, 7],
                [2, 6, 7],
                [3, 4, 5],
                [3, 4, 6],
                [3, 4, 7],
                [3, 5, 6],
                [3, 5, 7],
                [3, 6, 7],
                [4, 5, 6],
                [4, 5, 7],
                [4, 6, 7],
                [5, 6, 7],
            ],
        ),
    ],
)
def test_all_strictly_increasing_sequences_for(k, n, expected):
    recursive_algorithms.all_strictly_increasing_sequences.calls = 0

    returned = recursive_algorithms.all_strictly_increasing_sequences(k, n)

    assert len(expected) == len(
        returned
    ), f"Wrong answer for k={k} and n={n}. Expected={expected}. Returned={returned}."
    returned.sort()

    assert (
        returned == expected
    ), f"Wrong answer for k={k} and n={n}. Expected={expected}. Returned={returned}."
    if n >= k:
        assert (
            recursive_algorithms.all_strictly_increasing_sequences.calls >= n - k
        ), "Function all_strictly_increasing_sequences is not recursive"


def create_expected_pattern(n):
    half = [i for i in range(n, -5, -5)]
    return half + list(reversed(half[:-1]))


@pytest.mark.parametrize("n", [n for n in list(range(5)) + list(range(5, 20, 3))])
def test_create_pattern_for(n):
    recursive_algorithms.create_pattern.calls = 0

    expected = create_expected_pattern(n)
    returned = recursive_algorithms.create_pattern(n)

    assert (
        expected == returned
    ), f"Wrong answer for {n}. Expected: {expected}. Returned: {returned}."
    assert (
        recursive_algorithms.create_pattern.calls >= n // 5
    ), "Function create_pattern is not recursive"


@pytest.mark.parametrize("n", [n for n in list(range(5)) + list(range(5, 20, 3))])
def test_find_middle_for(n):
    recursive_algorithms.find_middle_rec.calls = 0

    elements = randlist(n)
    l = recursive_algorithms.LinkedList(elements)

    returned = recursive_algorithms.find_middle(l.root)
    if elements:
        expected = elements[n // 2]
        if returned:
            returned = returned.value
    else:
        expected = None

    assert (
        expected == returned
    ), f'Wrong answer for {"->".join(l)}. Expected: {expected}. Returned: {returned}.'
    assert (
        recursive_algorithms.find_middle_rec.calls >= n
    ), "Function find_middle_rec is not recursive"
