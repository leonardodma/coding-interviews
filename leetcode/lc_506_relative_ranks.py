from typing import List
import pytest


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexes = {}
        for i, s in enumerate(score):
            indexes[s] = i

        sorted_indexes = sorted(score, reverse=True)
        final_result = [None] * len(score)

        for i, s in enumerate(sorted_indexes):
            match i:
                case 0:
                    final_result[indexes[s]] = "Gold Medal"
                case 1:
                    final_result[indexes[s]] = "Silver Medal"
                case 2:
                    final_result[indexes[s]] = "Bronze Medal"
                case _:
                    final_result[indexes[s]] = str(i + 1)

        return final_result


# Testing
@pytest.mark.parametrize(
    "score, expected",
    [
        ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
        ([10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),
    ],
)
def test_findRelativeRanks(score, expected):
    assert Solution().findRelativeRanks(score) == expected
