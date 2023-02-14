from typing import List
import pytest


def binary_search(nums: List[int], target: int) -> int:
    """
    >>> binary_seach([1, 2, 3, 4, 5], 3)
    2
    >>> binary_seach([1, 2, 3, 4, 5], 6)
    -1
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Testing
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 6, -1),
    ],
)
def test_binary_search(nums, target, expected):
    assert binary_search(nums, target) == expected
